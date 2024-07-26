# Given an integer array nums of length n, you want to create an array and of length 2n where ans[i] == nums[i] and
# ans[i + n] == nums[i] for 0 <= i < n (0-indexed). Specifically, and is the concatenation of two nums arrays. Return
# the array ans.
#
# Example 1:
#
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array and is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:
#
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array and is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# 1. Understand the problem is asking us to concatenate an array with itself. The array is given as input. We need to
# return the concatenated array.
# 2. Plan: We can create a new array and append the elements of the given array twice to the new array. We can return
# the new array as the answer.

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return nums + nums

