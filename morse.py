#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code: Standard Edition
"""
__author__ = '???'

from morse_dict import MORSE_2_ASCII


def decode_morse(morse):
    # your code here
    return


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")

    print("\nCompleted.")
