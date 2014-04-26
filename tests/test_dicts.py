# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

import os
import os.path
import shutil
from tempfile import mkdtemp

import crosswords.dictionnaries as dicts

class TestDicts(unittest.TestCase):

    def setUp(self):
        self.path = mkdtemp()
        self._dictpath = dicts.DICTS_PATH
        dicts.DICTS_PATH = self.path + '/xde$a4l9'

    def tearDown(self):
        shutil.rmtree(self.path, ignore_errors=True)
        dicts.DICTS_PATH = self._dictpath

    # sanitize_word

    def test_sanitize_empty_word(self):
        self.assertEqual('', dicts.sanitize_word(''))

    def test_sanitize_ascii(self):
        self.assertEqual('foo', dicts.sanitize_word('foo'))

    def test_sanitize_case(self):
        self.assertEqual('fooo', dicts.sanitize_word('FoOO'))

    def test_sanitize_spaces(self):
        self.assertEqual('foobar', dicts.sanitize_word(' foo ba r  '))

    def test_sanitize_parentheses(self):
        self.assertEqual('foobar', dicts.sanitize_word('(a)foobar'))
        self.assertEqual('foobar', dicts.sanitize_word('foobar (one)'))

    # init_storage

    def test_init_storage_doesnt_exist(self):
        self.assertFalse(os.path.exists(dicts.DICTS_PATH))
        dicts.init_storage()
        self.assertTrue(os.path.exists(dicts.DICTS_PATH))

    def test_init_storage_exists(self):
        dicts.init_storage()
        self.assertTrue(os.path.exists(dicts.DICTS_PATH))
        dicts.init_storage()
        self.assertTrue(os.path.exists(dicts.DICTS_PATH))

    def test_init_storage_exists_as_file(self):
        os.makedirs(dicts.DICTS_PATH)
        dicts.DICTS_PATH += '/foobar'

        with open(dicts.DICTS_PATH, 'w') as f:
            f.write('nothing')

        self.assertRaises(OSError, dicts.init_storage)

    # local_list

    def test_local_list_empty(self):
        dicts.init_storage()
        self.assertSequenceEqual([], dicts.local_list())

    def test_local_list_one_timestamp(self):
        dicts.init_storage()
        with open(dicts.DICTS_PATH+'/foo.txt', 'w') as f:
            f.write("a\nword")

        lst = dicts.local_list()
        self.assertEqual(1, len(lst))
        self.assertEqual('foo', lst[0][0])

    def test_local_list_one_no_timestamp(self):
        dicts.init_storage()
        with open(dicts.DICTS_PATH+'/foo.txt', 'w') as f:
            f.write("a\nword")

        lst = dicts.local_list(timestamps=False)
        self.assertEqual(1, len(lst))
        self.assertEqual('foo', lst[0])

    # remote_list
    # update
    # download

    # exists

    def test_exists_no(self):
        self.assertFalse(dicts.exists('somerandomlanguage'))

    def test_exists_yes(self):
        dicts.init_storage()
        with open(dicts.DICTS_PATH+'/foo.txt', 'w') as f:
            f.write("a\nword")
        self.assertTrue(dicts.exists('foo'))
