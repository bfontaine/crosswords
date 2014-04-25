# -*- coding: UTF-8 -*-
from __future__ import print_function

import sys
from crosswords import dictionnaries
from crosswords.words import get_matches

def print_help_and_exit(exe='crosswords'):
    print("Usage:\n\t%s <word>" % exe)
    sys.exit(1)

def run(word=None):
    if len(sys.argv) < 2:
        print_help_and_exit(sys.argv[0])

    matches = get_matches(sys.argv[1], dictionnaries.DEFAULT)
    c = len(matches)

    if not matches:
        print("No word found.")
    else:
        print("%d possibilit%s:" % (c, 'y' if c == 1 else 'ies'))
        for match in matches:
            print('- %s' % match)
