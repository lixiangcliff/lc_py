class Solution(object):
    #nums

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

nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
#print obj.nums

print param_1
