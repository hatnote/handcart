
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
    print(ctx.search('lol', 'item'))
    print(ctx.search('instance', 'property'))
    print(ctx.get_entities(['P31', 'Q123']))


def get_candidate_map(csv_keys):
    '''return dictionary where example value is 
    {TaxonStatus: ['TaxonStatus', 'taxon', 'status', 'taxon status']}'''
    ret = {}
    candidate_field_list = []
    for key in csv_keys:
        candidates = []
        candidates.append(key)
        camel_case_key = strutils.camel2under(key)
        split_strings = camel_case_key.split('_')
        candidates.extend(split_strings)
        spaced_string = camel_case_key.replace("_", " ")
        candidates.append(spaced_string)
        candidates = list(set(candidates))  # dedupe
        candidates.sort(reverse=True, key=lambda x:len(x))
        candidate_field_list.append(ret)
        ret[key] = candidates
    return candidate_field_list

