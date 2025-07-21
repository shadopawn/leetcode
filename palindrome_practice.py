import unittest

def isPalindrome(word):
    reversedWord = ''
    for letter in word:
        reversedWord = letter + reversedWord
    return reversedWord == word

def isPalindromeAlt(word):
    return word[::-1] == word

class TestPalindrome(unittest.TestCase):

    def test_isPalindrome_0(self):
        self.assertTrue(isPalindrome("racecar"))

    def test_isPalindrome_1(self):
        self.assertFalse(isPalindrome("stuff"))
    
    def test_isPalindrome_2(self):
        self.assertTrue(isPalindrome("1232112321"))

    def test_isPalindrome_3(self):
        self.assertTrue(isPalindromeAlt("racecar"))

    def test_isPalindrome_4(self):
        self.assertFalse(isPalindromeAlt("stuff"))
    
    def test_isPalindrome_6(self):
        self.assertTrue(isPalindromeAlt("1232112321"))


if __name__ == '__main__':
    unittest.main()