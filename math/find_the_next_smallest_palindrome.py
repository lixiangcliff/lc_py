"""
http://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/

Given a number, find the next smallest palindrome larger than this number.
For example, if the input number is "2 3 5 4 5", the output should be "2 3 6 3 2".
 And if the input number is "9 9 9", the output should be "1 0 0 1".
"""


class Solution(object):

    def __init__(self):
        self.data = []


    def next_palindrome2(self, n):
        if n < 0:
            return 0
        n += 1
        lst = list(str(n))
        i = 0
        j = int(len(lst)) - 1
        while i < j:
            if lst[i] < lst[j]:
                lst[j - 1] = str(int(lst[j - 1]) + 1)
            lst[j] = lst[i]
            i += 1
            j -= 1
        return int(''.join(lst))


    def next_palindrome(self, s):
        if s is None or len(s) == 0:
            return '0'

        if self.is_all_nine(s):
            return str(int(s) + 2)

        length = len(s)
        is_even = length % 2 == 0

        if self.is_palindrome(s):
            if is_even:
                first_half = str(int(s[:length / 2]) + 1)
                return first_half + first_half[::-1]
            else:
                first_half = str(int(s[:(length + 1) / 2]) + 1)
                return first_half + first_half[:length / 2][::-1]

        if is_even:
            first_half = s[:length / 2]
            sec_half = s[length / 2:]
            if int(first_half[::-1]) < int(sec_half):
                first_half = str(int(first_half) + 1)
            return first_half + first_half[::-1]
        else:
            first_half = s[:(length - 1) / 2]
            sec_half = s[(length + 1) / 2:]
            if int(first_half[::-1]) < int(sec_half):
                first_half = str(int(s[:(length + 1) / 2]) + 1)
            else:
                first_half = s[:(length + 1) / 2]
            return first_half + first_half[::-1][1:]

    def is_palindrome(self, s):
        if s is None or len(s) == 0:
            return False

        length = len(s)
        for i in range (length / 2):
            if s[i] != s[length - 1 - i]:
                return False
        return True

    def is_all_nine(self, s):
        if s is None or len(s) == 0:
            return False

        for i in s:
            if i != '9':
                return False
        return True

obj = Solution()

n = 111111
print obj.next_palindrome2(n)

s = str(n)
print obj.next_palindrome(s)
