# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

import shutil
import os.path
from tempfile import mkdtemp

from crosswords import words
from crosswords.words import dicts

class TestWords(unittest.TestCase):

    def setUp(self):
        self.path = mkdtemp()
        self._dictpath = dicts.DICTS_PATH
        dicts.DICTS_PATH = self.path + '/xde$a4l9'
        dicts.init_storage()
        with open(dicts.filepath('foo'), 'w') as f:
            f.write("abc\ndef\nghi\nwxxx\nwxxx")

    def tearDown(self):
        shutil.rmtree(self.path, ignore_errors=True)
        dicts.DICTS_PATH = self._dictpath

    # compile_pattern

    def test_compile_empty_word(self):
        r = words.compile_pattern('')

        self.assertNotEqual(None, r.match(''))
        self.assertEqual(None, r.match('a'))

    def test_compile_full_word(self):
        w = 'foobar'
        r = words.compile_pattern(w)

        self.assertNotEqual(None, r.match(w))
        self.assertEqual(None, r.match('qux'))
        self.assertEqual(None, r.match(''))

    def test_compile_partial_word(self):
        w = 'foobar'
        r = words.compile_pattern('fo??ar')

        self.assertNotEqual(None, r.match('foobar'))
        self.assertNotEqual(None, r.match('footar'))
        self.assertEqual(None, r.match('fooobar'))
        self.assertEqual(None, r.match('afoobar'))
        self.assertEqual(None, r.match('foobara'))

    def test_compile_partial_sanitized_word(self):
        w = 'foobar'
        r = words.compile_pattern('  Fo??a-R')

        self.assertNotEqual(None, r.match('foobar'))
        self.assertNotEqual(None, r.match('footar'))
        self.assertEqual(None, r.match('fooobar'))
        self.assertEqual(None, r.match('afoobar'))
        self.assertEqual(None, r.match('foobara'))

    # get_matches

    def test_get_no_matches(self):
        self.assertSequenceEqual([], words.get_matches('foo', 'foo'))

    def test_get_limited_matches(self):
        self.assertSequenceEqual(['abc'], words.get_matches('???', 'foo', 1))

    def test_get_matches(self):
        self.assertSequenceEqual(['abc', 'def', 'ghi'],
                                 words.get_matches('???', 'foo'))

    def test_get_matches_no_duplicates(self):
        self.assertSequenceEqual(['wxxx'], words.get_matches('wxx?', 'foo'))
