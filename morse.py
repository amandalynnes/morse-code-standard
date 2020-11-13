#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code: Standard Edition
"""
__author__ = 'Amanda Simmons, Mike Boring, and Daniel Lomelina'

from morse_dict import MORSE_2_ASCII


def decode_morse(morse):
    # your code here
    # decoded = ''
    morse_words = morse.split('   ')
    # morse_2 = ''
    decoded_letters = []
    for word in morse_words:
        # decoded += MORSE_2_ASCII(char)
        letters = word.split()
        for letter in letters:
            decoded_letters.append(MORSE_2_ASCII[letter])
        decoded_letters.append(' ')

    return ''.join(decoded_letters).strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")

    print("\nCompleted.")
