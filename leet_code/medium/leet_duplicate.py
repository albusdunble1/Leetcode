class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        found = set()
        output = []
        
        for i in range(len(nums)):
            if nums[i] in found:
                output.append(nums[i])
            else:
                found.add(nums[i])
        
        return output


#https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/