# -*- coding: UTF-8 -*-

import re
from unidecode import unidecode

def compile_pattern(word):
    """
    take a word pattern and return a Python regexp. A word pattern is a word
    with unknown letters replaced by a '?', e.g. 'di?ti??nar?'.
    """

    # use an unicode string for `unidecode`
    if type(word) == str:
        word = word.decode()

    # remove trailing spaces
    word = word.strip()
    # remove accents, hyphens & other special chars
    word = re.sub(r'["\'-;.]+', '', unidecode(word))
    # only lowercase
    word = word.lower()

    # make it a regexp pattern
    return re.compile(r'^%s$' % re.sub(r'\?', '[a-z]', word))


def get_matches(pattern, filename, max_count=8):
    """
    take a word pattern or a Python regexp and a filename for the dictionnary,
    and return a list of all matching words.

    The dictionnary file should contain only one word per line, lowercase with
    no accents nor hyphens.
    """
    if str(pattern) == pattern:
        pattern = compile_pattern(pattern)

    results = []

    with open(filename, 'r') as f:
        for word in f:
            if max_count <= 0:
                break
            w = word.strip()
            if pattern.match(w):
                results.append(w)
                max_count -= 1

    return results
