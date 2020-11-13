#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# flake8: noqa
"""
Unit tests for Morse Code.

Students should not modify this file.
"""
__author__ = 'madarp'

import sys
import unittest
import importlib
import subprocess

# suppress __pycache__ and .pyc files
sys.dont_write_bytecode = True

# Kenzie devs: change this to 'soln.morse' to test solution
PKG_NAME = 'morse'

# some handy morse strings
# HEY JUDE
morse_hey_jude = '.... . -.--   .--- ..- -.. .'
# THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
morse_quick_fox = '- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-'


class TestDecodeMorse(unittest.TestCase):
    """Only tests the decode_morse() function"""

    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        cls.module = importlib.import_module(PKG_NAME)

    def test_hey_jude(self):
        """Check basic HEY JUDE"""
        actual = self.module.decode_morse(morse_hey_jude)
        self.assertEqual(actual, 'HEY JUDE')

    def test_basic_letters(self):
        """Check Basic Morse decoding"""
        self.assertEqual(self.module.decode_morse('.-'), 'A')
        self.assertEqual(self.module.decode_morse('.'), 'E')
        self.assertEqual(self.module.decode_morse('..'), 'I')
        self.assertEqual(self.module.decode_morse('. .'), 'EE')
        self.assertEqual(self.module.decode_morse('.   .'), 'E E')
        self.assertEqual(self.module.decode_morse('...---...'), 'SOS')
        self.assertEqual(self.module.decode_morse('... --- ...'), 'SOS')
        self.assertEqual(self.module.decode_morse('...   ---   ...'), 'S O S')

    def test_extra_spaces(self):
        """Check handling of spaces"""
        self.assertEqual(self.module.decode_morse(' . '), 'E')
        self.assertEqual(self.module.decode_morse('   .   . '), 'E E')

    def test_complex(self):
        """Check long message decoding"""
        morse = '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .  '            ' .-.. .- --.. -.--   -.. --- --. .-.-.-  '
        actual = self.module.decode_morse(morse)
        self.assertEqual(actual, 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)

    def test_author_string(self):
        """Checking for __author__ string"""
        self.assertNotEqual(self.module.__author__, '???')


if __name__ == '__main__':
    unittest.main(verbosity=2)
