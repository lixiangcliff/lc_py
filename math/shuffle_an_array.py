"""
https://leetcode.com/problems/shuffle-an-array/
384. Shuffle an Array

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
from random import randint


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffled_nums = []
        copied_nums = list(self.nums)
        while copied_nums:
            shuffled_nums.append(copied_nums.pop(randint(0, len(copied_nums) - 1)))
        return shuffled_nums


"""
A hacky way
https://discuss.leetcode.com/topic/54049/python-hack

    def __init__(self, nums):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))

"""

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print param_1
print param_2