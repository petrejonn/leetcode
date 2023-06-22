#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        """
        result = 0
        for num in nums:
            result ^= num
        return result




        
# @lc code=end

