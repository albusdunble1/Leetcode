class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        snums = set(nums)
        
        for num in snums:
            if nums.count(num) > len(nums)/2:
                return num
                
        
#https://leetcode.com/problems/majority-element/