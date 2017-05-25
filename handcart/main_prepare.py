
PREPARE_HELP = ""
PREPARE_DESC = PREPARE_HELP + "\n\n"


def load_csv(file_name):
    pass


def configure_parser(subparsers):
    prep_prs = subparsers.add_parser('prepare',
                                     description=PREPARE_DESC,
                                     help=PREPARE_HELP)
    add_arg = prep_prs.add_argument
    add_arg('--file')
    add_arg('--prep_file')

    prep_prs.set_defaults(func=execute)


def execute(ctx):
    print(ctx.http_client.headers)

    print(ctx.urls.search('lol', 'item'))
    print(ctx.urls.get_entities(['P12', 'Q123']))
