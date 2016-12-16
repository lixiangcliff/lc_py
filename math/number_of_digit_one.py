"""
233. Number of Digit One

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

"""

import math

class Solution(object):


    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        length = len(n)
        res = 0
        while n:
            val = n[0] - '0'
            count = val - 1
            res += count * pow(10, )
