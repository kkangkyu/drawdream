class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [2, 7, 11, 15]
        target = 9
        # for i in range(nums):
        #     for j in (nums):
        #         if i + j == target:
        #             return [nums.index(i), nums.index(j)]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
