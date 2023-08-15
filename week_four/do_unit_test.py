"""
Run a test using a function that would return the result of 2 parameters. 
(Don't use the sum() function.)


Write a test case to check if the value 42 is present in the list [10, 20, 30, 40, 42]
"""

import unittest


def add_numbers(a:int, b:int) -> int:
    return a+b


class TestAdd(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(4, 5), 9)
        self.assertEqual(add_numbers(10, 5), 15)


class TestMembership(unittest.TestCase):
    def test_membership(self):
        self.assertIn(42, [10, 20, 30, 40, 42])


if __name__ == "__main__":
    unittest.main()
