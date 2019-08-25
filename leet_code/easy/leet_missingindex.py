class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp = set(i for i in range(len(nums)+1))
                
        return list(temp-set(nums))[0]
    
        # slower but more intuitive approach (3x slower)
        
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i


#https://leetcode.com/problems/missing-number/