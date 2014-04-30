# -*- coding: UTF-8 -*-

import re
import crosswords.dictionnaries as dicts


def compile_pattern(word):
    """
    take a word pattern and return a Python regexp. A word pattern is a word
    with unknown letters replaced by a '?', e.g. 'di?ti??nar?'.
    """
    return re.compile(r'^%s$' % re.sub(r'\?', '[a-z]',
                                       dicts.sanitize_word(word)))


def get_matches(pattern, language, max_count=8):
    """
    take a word pattern or a Python regexp and a language name, and return a
    list of all matching words.
    """
    if str(pattern) == pattern:
        pattern = compile_pattern(pattern)

    results = []

    if not dicts.exists(language):
        print("The language '%s' is not available locally." % language)
        return []

    with open(dicts.filepath(language), 'r') as f:
        for word in f:
            if max_count <= 0:
                break
            w = word.strip()
            if pattern.match(w) and w not in results:
                results.append(w)
                max_count -= 1

    return results
