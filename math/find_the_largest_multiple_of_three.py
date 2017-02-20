"""
http://www.geeksforgeeks.org/find-the-largest-number-multiple-of-3/

Given an array of non-negative integers. Find the largest multiple of 3 that can be formed from array elements.
For example, if the input array is {8, 1, 9}, the output should be "9 8 1", and if the input array is {8, 1, 7, 6, 0},
output should be "8 7 6 0".
"""
import heapq

class Solution(object):
    def __init__(self):
        pass


    def largest_multiple_of_three(self, num):
        if not num:
            return [0]
        remainder_one = []
        remainder_two = None
        num = sorted(num, reverse=True)
        sum = 0;
        for n in num:
            if n % 3 == 1:
                if len(remainder_one) < 2:
                    heapq.heappush(remainder_one, n)
                else:
                    heapq.heappushpop(remainder_one, n)

            elif n % 3 == 2:
                if not remainder_two or remainder_two and remainder_two < n:
                    remainder_two = n

            sum += n

        if sum % 3 == 1:
            if remainder_one:
                num.remove(heapq.heappop(remainder_one))
            else:
                num = [0]
        elif sum % 3 == 2:
            if remainder_two:
                num.remove(remainder_two)
            elif len(remainder_one) == 2:
                num.remove(remainder_one[0])
                num.remove(remainder_one[1])
            else:
                num = [0]

        return num


obj = Solution()

num = [1,2,3,4,5,7]
print obj.largest_multiple_of_three(num)





