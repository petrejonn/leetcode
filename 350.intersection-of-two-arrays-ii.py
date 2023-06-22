#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}
        result = []
        hm=Counter(nums1)
        for i in nums2:
            if hm.get(i,0)>0:
                result.append(i)
                hm[i] -= 1   
        return result
            
        
# @lc code=end

