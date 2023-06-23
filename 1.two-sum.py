#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        for i in range(len(nums)):
            if target-nums[i] in nums_map and i!=nums_map[target-nums[i]]:
                return [nums_map[target-nums[i]],i]
            nums_map[nums[i]]=i
            
            
        
# @lc code=end

