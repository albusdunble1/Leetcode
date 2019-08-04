class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        

        count = 0
        
        i = 0
        while i < len(nums):
            if not nums[i]:
                nums.pop(i)
                count += 1
                i -= 1
            i += 1
        
        for i in range(count):
            nums.append(0)


#https://leetcode.com/problems/move-zeroes/