# https://leetcode.com/problems/word-search/

import unittest
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row_index, row in enumerate(board):
            for column_index in range(len(row)):
                if self.found_word_at(board, word, row_index, column_index):
                    return True
        return False

    def found_word_at(self, board: List[List[str]], word: str, row: int, column: int) -> bool:
        if not word:
            return True

        if self.out_of_bounds(board, row, column):
            return False

        current_letter = board[row][column]

        if current_letter is not word[0]:
            return False

        # Set the board at position to "" to act as marking visited
        board[row][column] = ""

        found = (self.found_word_at(board, word[1:], row - 1, column) or
                 self.found_word_at(board, word[1:], row, column + 1) or
                 self.found_word_at(board, word[1:], row + 1, column) or
                 self.found_word_at(board, word[1:], row, column - 1))

        # Reset letter after doing recursive search
        board[row][column] = current_letter

        return found

    def out_of_bounds(self, board, row, column):
        return self.row_out_of_bounds(board, row) or self.column_out_of_bounds(board, column)

    def row_out_of_bounds(self, board, row):
        max_row_index = len(board) - 1
        return not 0 <= row <= max_row_index

    def column_out_of_bounds(self, board, column):
        max_column_index = len(board[0]) - 1
        return not 0 <= column <= max_column_index


class TestWordSearch(unittest.TestCase):

    def test_word_search(self):
        word_search = Solution()
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ]
        word = "ABCCED"
        self.assertTrue(word_search.exist(board, word))

if __name__ == '__main__':
    unittest.main()
