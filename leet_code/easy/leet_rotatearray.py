class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # original solution (less efficient)
        # i = 0
        # while i < k:
        #     nums.insert(0,nums.pop())
        #     i += 1
        
        # 50% my idea
        tail = nums[len(nums)-k:]
        head = nums[:len(nums)-k]
        nums[:len(tail)] = tail
        nums[len(tail):] = head


#https://leetcode.com/problems/rotate-array/