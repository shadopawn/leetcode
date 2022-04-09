'''
Given two string note and magazine, return true if note can be constructed from magazine and false other wise.
Each letter in magazine can only be used once in note. 
'''

import unittest
from collections import Counter
import string
import random


def can_make_note_from_magazine(note, magazine):
    note_count = Counter(note)
    magazine_count = Counter(magazine)
    for letter, count in note_count.items():
        if count > magazine_count[letter]:
            return False
    return True


class TestNoteMaking(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.MAX_MAGAZINE_LENGTH = 1000
        cls.alphabet = string.ascii_letters + string.digits
        cls.can_not_make_note_parameters = [
            ("a", "b"),
            ("aa", "ab"),
            ("abcdef", "bcdefg"),
            ("alogiknbjaol", "asdjkfb"),
            ("qtpAZZ11", cls.alphabet),
            (cls.alphabet + "a", cls.alphabet),
            ("1", ""),
            ("asdf", ""),
            (" ", ""),
        ]

    def test_can_make_note_from_magazine(self):
        for _ in range(100):
            note, magazine = self.create_random_note_for_magazine()
            with self.subTest(note=note, magazine=magazine):
                self.assertTrue(can_make_note_from_magazine(note, magazine))

    def test_can_not_make_note_from_magazine(self):
        for note, magazine in self.can_not_make_note_parameters:
            with self.subTest(note=note, magazine=magazine):
                self.assertFalse(can_make_note_from_magazine(note, magazine))

    def create_random_note_for_magazine(self):
        magazine = self.create_random_magazine()
        note_length = random.randint(0, len(magazine))
        note = "".join(random.sample(magazine, note_length))
        return note, magazine

    def create_random_magazine(self):
        magazine_length = random.randint(0, self.MAX_MAGAZINE_LENGTH)
        return "".join(random.choice(self.alphabet) for _ in range(magazine_length))


if __name__ == "__main__":
    unittest.main(verbosity=2)
