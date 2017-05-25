
if __name__ != '__main__':
    raise ImportError('__main__.py cannot be imported')

import sys
import argparse
import importlib

from handcart import core


def main(argv):
    prs = argparse.ArgumentParser(description="project-oriented,"
                                  " repeatable Wikidata uploads")
    subparsers = prs.add_subparsers(metavar='command', dest='cmd')

    # http://bugs.python.org/issue9253
    # http://stackoverflow.com/a/18283730/1599393
    subparsers.required = True

    mod_names = ['prepare']
    fq_mod_names = ["handcart.main_" + suffix for suffix in mod_names]
    for mod_name in fq_mod_names:
        module = importlib.import_module(mod_name)
        module.configure_parser(subparsers)

    args = prs.parse_args()
    args.argparser = prs
    hc = core.Handcart(args=args)

    return args.func(hc) or 0


try:
    sys.exit(main(sys.argv))
except Exception:
    import pdb;pdb.post_mortem()
    raise
