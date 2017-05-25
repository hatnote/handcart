
PREPARE_HELP = ""
PREPARE_DESC = PREPARE_HELP + "\n\n"


def load_csv(file_name):
    pass


def search_wikidata(search, wd_type, language='en'):
    # Search for a wikidata item by label
    # wd_type can be 'item' or 'property'
    # https://www.wikidata.org/w/api.php?action=wbsearchentities&search=instance%20of&language=en&type=property&format=jsonfm
    pass


def get_wikidata_entities(wd_ids):
    #https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q42%7CP17
    pass


def configure_parser(subparsers):
    prs = subparsers.add_parser('prepare')

    prep_prs = subparsers.add_parser('prepare',
                                     description=PREPARE_DESC,
                                     help=PREPARE_HELP)
    add_arg = prep_prs.add_argument
    add_arg('--file')
    add_arg('--prep_file')

    prep_prs.set_defaults(func=execute)


def execute(ctx):
    print(ctx.http_client.headers)
