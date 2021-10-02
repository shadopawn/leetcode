# https://leetcode.com/problems/word-search/

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for rowIndex, row in enumerate(board):
            for columnIndex in range(len(row)):
                if self.foundWordAt(board, word, rowIndex, columnIndex):
                    return True
        return False
    
    def foundWordAt(self, board: List[List[str]], word: str, row: int, column: int) -> bool:
        if not word:
            return True
             
        if self.outOfBounds(board, row, column):
            return False
        
        currentLetter = board[row][column]
        
        if currentLetter is not word[0]:
            return False
        
        board[row][column] = ""
        
        found = (self.foundWordAt(board, word[1:], row - 1, column) or 
                 self.foundWordAt(board, word[1:], row, column + 1) or
                 self.foundWordAt(board, word[1:], row + 1, column) or
                 self.foundWordAt(board, word[1:], row, column - 1))
        
        board[row][column] = currentLetter
        
        return found
        
    def outOfBounds(self, board, row, column):
        return self.rowOutOfBounds(board, row) or self.columnOutOfBounds(board, column)
    
    def rowOutOfBounds(self, board, row):
        maxRowIndex = len(board) - 1
        return not 0 <= row <= maxRowIndex
        
    def columnOutOfBounds(self, board, column):
        maxColumnIndex = len(board[0]) - 1
        return not 0 <= column <= maxColumnIndex