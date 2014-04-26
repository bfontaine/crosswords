# -*- coding: UTF-8 -*-

import sys
import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

from crosswords import cli

class TestWords(unittest.TestCase):

    def setUp(self):
        self._argv = sys.argv
        self._exit = sys.exit
        sys.exit = lambda s: None

    def tearDown(self):
        sys.argv = self._argv
        sys.exit = self._exit


    # print_help_and_exit
    # find_word
    # print_languages_and_exit

    # extract_opts

    def test_extract_opts_no_opts(self):
        sys.argv = ['', '--foo', 'bar', '-q', 't']
        self.assertEqual(0, len(cli.extract_opts().keys()))

    def test_extract_opts_default(self):
        v = 42
        sys.argv = ['', '-a']
        opts = cli.extract_opts(a=v)
        self.assertSequenceEqual(['a'], opts.keys())
        self.assertEqual(v, opts['a'])

    def test_extract_opts_not_here(self):
        v = 42
        sys.argv = ['', '-b']
        opts = cli.extract_opts(a=v)
        self.assertSequenceEqual(['a'], opts.keys())
        self.assertEqual(v, opts['a'])

    def test_extract_opts(self):
        v = '17'
        sys.argv = ['', '-a', v]
        opts = cli.extract_opts(a=24)
        self.assertSequenceEqual(['a'], opts.keys())
        self.assertEqual(v, opts['a'])

    # run
