
import os
import socket
import hashlib
from collections import namedtuple

import attr
import requests
import unicodecsv
from hyperlink import URL
from boltons import strutils


VERSION = '0.1'

WIKIDATA_API_BASE = 'https://www.wikidata.org/w/api.php'
example_file = 'example_data/taxon_treatments_2010s.csv'

Item = namedtuple('Item', ['id', 'label', 'description'])
Property = namedtuple('Property', ['id', 'label', 'description', 'datatype'])


def to_unicode(obj):
    try:
        return unicode(obj)
    except UnicodeDecodeError:
        return unicode(obj, encoding='utf8')

to_u = to_unicode


@attr.s
class URLManager(object):
    api_base = attr.ib(default=WIKIDATA_API_BASE)

    def search(self, target, wd_type='item', lang='en'):
        if wd_type not in ('property', 'item'):
            raise ValueError('wd_type expected one of property or item, not %r'
                             % wd_type)
        url = URL.from_text(self.api_base)
        url = (url
               .set(u'action', u'wbsearchentities')
               .set(u'type', to_u(wd_type))
               .set(u'search', to_u(target))
               .set(u'language', to_u(lang))
               .set(u'format', u'json'))
        return url.to_text()

    def get_entities(self, ids):  # TODO: lang?
        url = URL.from_text(self.api_base)
        url = (url
               .set(u'action', u'wbgetentities')
               .set(u'ids', u'|'.join([to_u(wd_id) for wd_id in ids]))
               .set(u'format', u'json'))
        return url.to_text()


def get_user_hash():
    user = socket.gethostname()
    try:
        import getpass
        user += getpass.getuser()
    except:
        try:
            user += str(os.getuid())
        except:
            pass
    return hashlib.sha256(user).hexdigest()[:24]


@attr.s
class Handcart(object):
    args = attr.ib()
    urls = attr.ib(default=URLManager())  # TODO
    lang = 'en' # TODO: We could have a separate language in different
                # parts of the application

    def __attrs_post_init__(self):
        self.http_client = requests.Session()
        user_hash = get_user_hash()
        user_agent = 'hatnote-handcart/%s (user:%s)' % (VERSION, user_hash)
        self.http_client.headers.update({'User-Agent': user_agent})

    def search(self, target, wd_type='item', lang=lang):
        search_url = self.urls.search(target, wd_type, lang)
        resp = requests.get(search_url)
        data = resp.json()
        ret = []
        for res in data['search']:
            # Will search always return the same entity type?
            if wd_type == u'item':
                ret.append(Item(res['id'], res['label'], res['description']))
            elif wd_type == u'property':
                ret.append(Property(res['id'], res['label'],
                                    res['description'], res['datatype']))
        return ret

    def get_entities(self, ids):
        get_entities_url = self.urls.get_entities(ids)
        resp = requests.get(get_entities_url)
        data = resp.json()
        ret = {}
        for entity_id in ids:
            entity = data['entities'][entity_id]
            if entity_id[0] == 'Q':
                label = entity['labels'][self.lang]
                description = entity['descriptions'][self.lang]
                ret[entity_id] = Item(entity_id, label, description)
            elif entity_id[0] == 'P':
                label = entity['labels'][self.lang]
                description = entity['descriptions'][self.lang]
                datatype = entity['datatype']
                ret[entity_id] = Property(entity_id, label, description, 
                                          datatype)
        return ret


def get_csv(csv_file):
    reader = unicodecsv.DictReader(open(example_file, 'rb'))
    return list(reader)


def get_csv_headers(csv_file):
    example_csv = get_csv(example_file)[0]
    csv_keys = example_csv.keys()
    return csv_keys
