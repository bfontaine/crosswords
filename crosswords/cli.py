# -*- coding: UTF-8 -*-
from __future__ import print_function

import sys
import crosswords
from crosswords.words import get_matches
import crosswords.dictionnaries as dicts


def print_help_and_exit(exe='crosswords'):
    print("Usage:\n\t%s [-l <language>] <word>\n" % exe)
    print("""\
Additionnally, some words have a special meaning:
  install:     install a new language
  list:        list local languages
  remote_list: list installable languages
  update:      update local languages""")
    sys.exit(1)


def find_word(word, dictionnary):
    matches = get_matches(word, dictionnary)
    c = len(matches)

    if not matches:
        print("No word found.")
    else:
        print("%d possibilit%s:" % (c, 'y' if c == 1 else 'ies'))
        for match in matches:
            print('- %s' % match)


def print_languages_and_exit(lst, status=1, header=True):
    """print a list of languages and exit"""
    if header:
        print("Available languages:")
    for lg in lst:
        print("- %s" % lg)
    sys.exit(status)


def extract_opts(**opts):
    """
    Small utility to extract a set of one-char options from sys.argv.
    """
    values = {}
    for opt, init in opts.items():
        try:
            idx = sys.argv.index('-%s' % opt)
        except ValueError:
            continue
        if idx+1 < len(sys.argv):
            opts[opt] = sys.argv.pop(idx+1)

        sys.argv.pop(idx)

    return opts


def run(word=None):
    opts = extract_opts(l=dicts.DEFAULT)

    argc = len(sys.argv)
    if argc < 2:
        print_help_and_exit(sys.argv[0])

    word = sys.argv[1]

    if word == 'update':
        dicts.update(verbose=True)

    elif word == 'install':
        lst = dicts.remote_list(timestamps=False)
        if argc < 3:
            print("Usage:\n\t%s install <language>" % sys.argv[0])
            print_languages_and_exit(lst)

        lg = sys.argv[2].strip().lower()
        if lg not in lst:
            print("The language '%s' is not available." % lg)
            print_languages_and_exit(lst)
        dicts.download(lg)

    elif word == 'list':
        print("Locally available languages:")
        print_languages_and_exit(dicts.local_list(timestamps=False),
                                 status=0, header=False)
        print("Use 'remote_list' to list remotely available languages.")

    elif word == 'remote_list':
        print("Remotely available languages:")
        print_languages_and_exit(dicts.remote_list(timestamps=False),
                                 status=0, header=False)
        print("Use 'install <language>' to download and install a language.")

    elif word == '--version':
        print("Crosswords v%s" % crosswords.__version__)

    else:
        matches = find_word(word, opts['l'])
