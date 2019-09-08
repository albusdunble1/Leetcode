class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxi = nums.index(max(nums))
        
        for i in range(len(nums)):
            if i != maxi:
                if max(nums) < nums[i]*2:
                    return -1
        
        return maxi


#         another slightly shorter solution

#         maxi = nums.index(max(nums))
#         temp = max(nums)
#         nums[maxi] = -1
        
#         return maxi if temp >= max(nums)*2 else -1


#https://leetcode.com/problems/largest-number-at-least-twice-of-others/