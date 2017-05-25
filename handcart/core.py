
import os
import socket
import hashlib

import attr
import requests

VERSION = '0.1'


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

    def __attrs_post_init__(self):
        self.http_client = requests.Session()
        user_hash = get_user_hash()
        user_agent = 'hatnote-handcart/%s (user:%s)' % (VERSION, user_hash)
        self.http_client.headers.update({'User-Agent': user_agent})
