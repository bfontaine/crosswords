# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

from crosswords import words

class TestWords(unittest.TestCase):

    pass # TODO
