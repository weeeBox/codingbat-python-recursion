from unittest import TestCase
from typing import List


def split53(nums: List[int]) -> bool:
    """
    Given an array of ints, is it possible to divide the ints into two groups, so that the sum of the two groups is the
    same, with these constraints: all the values that are multiple of 5 must be in one group, and all the values that
    are a multiple of 3 (and not a multiple of 5) must be in the other. (No loops needed.)
    
    Examples:
    split53([1, 1]) → true
    split53([1, 1, 1]) → false
    split53([2, 4, 2]) → true
    """
    pass


class Test(TestCase):
    def test1(self):
        self.assertTrue(split53([1, 1]))

    def test2(self):
        self.assertFalse(split53([1, 1, 1]))

    def test3(self):
        self.assertTrue(split53([2, 4, 2]))

    def test4(self):
        self.assertFalse(split53([2, 2, 2, 1]))

    def test5(self):
        self.assertTrue(split53([3, 3, 5, 1]))

    def test6(self):
        self.assertFalse(split53([3, 5, 8]))

    def test7(self):
        self.assertTrue(split53([2, 4, 6]))
