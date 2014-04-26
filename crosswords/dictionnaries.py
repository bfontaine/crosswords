# -*- coding: UTF-8 -*-
from __future__ import print_function

import os
import os.path
import errno
from glob import glob
from unidecode import unidecode
import re
import requests

DICTS_URL = 'http://bfontaine.net/crosswords/dicts'
DICTS_PATH = os.path.join(os.path.expanduser('~'), '.crosswords', 'dicts')

DEFAULT = 'french'


def sanitize_word(word):
    """
    sanitize a word by removing its accents, special characters, etc
    """
    # use an unicode string for `unidecode`
    if type(word) == str:
        try:
            word = word.decode()
        except AttributeError:
            pass # Python3

    # remove trailing spaces
    word = word.strip()
    # remove accents, hyphens & other special chars
    word = re.sub(r'[ "\'-;.]+', '', unidecode(word))
    # only lowercase
    return word.lower()


def init_storage():
    """
    Initialize the local dictionnaries cache in ~/.crosswords/dicts.
    """
    # http://stackoverflow.com/a/600612/735926
    try:
        os.makedirs(DICTS_PATH)
    except OSError as ex:
        if ex.errno != errno.EEXIST or not os.path.isdir(DICTS_PATH):
            raise


def local_list(timestamps=True):
    """
    Return a list of the locally available dictionnaries. Each element is a
    tuple of the dictionnary name and its last modification date as a
    timestamp.
    """
    init_storage()
    lst = []
    for d in glob(os.path.join(DICTS_PATH, '*.txt')):
        name = d.split('/')[-1].replace('.txt', '')
        lst.append((name, os.path.getmtime(d)) if timestamps else name)

    return lst


def remote_list(timestamps=True):
    """
    Return a list of the remotely available dictionnaries. Each element is a
    tuple of the dictionnary name and its last modification date as a
    timestamp.
    """
    r = requests.get(DICTS_URL)
    lst = []
    for f in r.text.split('\n'):
        if not f:
            continue
        name, date = f.split(':')
        name = name.replace('.txt', '')
        lst.append((name, int(date)) if timestamps else name)

    return lst


def update(verbose=False):
    """
    Update local dictionnaries by downloading the latest version from the
    server, if there's one.
    """
    local = local_list()
    remote = dict(remote_list())

    updated = False

    for name, date in local:
        if name in remote and remote[name] > date:
            updated = True
            if verbose:
                print("Updating '%s'..." % name)
            download(name)

    if not updated and verbose:
        print("Nothing to update.")


def download(name, verbose=False):
    """
    Download a dictionnary from the remote server into the local cache. Return
    the number of new words or -1 on error.
    """
    init_storage()

    if verbose:
        print("Downloading '%s'..." % name)
    r = requests.get('%s/%s.txt' % (DICTS_URL, name))

    if r.status_code != 200:
        return -1

    wcount = 0

    with open(os.path.join(DICTS_PATH, '%s.txt' % name), 'w') as f:
        for word in r.iter_lines():
            wcount += 1
            f.write('%s\n' % sanitize_word(word))

    if verbose:
        print("%d words added." % wcount)
    return wcount


def filepath(language):
    """return a file path for a given language"""
    return os.path.join(DICTS_PATH, '%s.txt' % language)

def exists(language):
    """test if a dictionnary for the given language exists locally"""
    return os.path.exists(filepath(language))
