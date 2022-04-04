# https://leetcode.com/problems/palindrome-linked-list/

import unittest
import random


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    middle = find_middle(head)

    second_half_reverse_head = reverse_list(middle)

    while head and second_half_reverse_head:
        if head.value != second_half_reverse_head.value:
            return False
        head = head.next
        second_half_reverse_head = second_half_reverse_head.next

    return True

def find_middle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_list(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


class TestIsPalindromicLinkedList(unittest.TestCase):

    def test_is_palindromic_linked_list(self):
        for _ in range(100):
            head = self.create_palindromic_linked_list()
            with self.subTest():
                self.assertTrue(is_palindromic_linked_list(head))

    def test_is_not_palindromic_linked_list(self):
        for _ in range(100):
            head = self.create_non_palindromic_linked_list()
            with self.subTest():
                self.assertFalse(is_palindromic_linked_list(head))

    def create_palindromic_linked_list(self):
        palindrome_list = self.create_palindromic_list()
        return self.cerate_linked_list(palindrome_list)

    def create_non_palindromic_linked_list(self):
        non_palindrome_list = self.create_random_list()
        # Ensure random list isn't a palindrome
        non_palindrome_list.append(non_palindrome_list[0] + 1)
        return self.cerate_linked_list(non_palindrome_list)

    def create_palindromic_list(self):
        random_numbers = self.create_random_list()
        return random_numbers + random_numbers[::-1]

    def create_random_list(self):
        total_nodes = random.randint(1, 1000)
        return [random.randint(-100, 100) for _ in range(total_nodes)]

    def cerate_linked_list(self, values):
        head = Node(values[0])
        current = head
        for value in values[1:]:
            new_node = Node(value)
            current.next = new_node
            current = new_node
        return head


if __name__ == "__main__":
    unittest.main(verbosity=2)
