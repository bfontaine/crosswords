# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

import crosswords.dictionnaries as dicts

class TestDicts(unittest.TestCase):

    # sanitize_word

    def test_sanitize_empty_word(self):
        self.assertEqual('', dicts.sanitize_word(''))

    # init_storage
    # local_list
    # remote_list
    # update
    # download
    # exists
