class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """



#       ==================== 2ND MOST EFFICIENT (ORIGINAL) ====================
#         consec = []
#         count = 0
        
#         for num in nums:
#             if num:
#                 count += 1
#             else:
#                 consec.append(count)
#                 count = 0
                
#             if num == nums[len(nums)-1] and num:
#                 consec.append(count)
                
#         return max(consec)



#       ==================== LEAST EFFICIENT ====================
#         consec = []
    
#         if 0 not in nums:
#             return len(nums)
#         elif 1 not in nums:
#             return 0
        
#         while 0 in nums:
#             if nums.index(0) != 0:
#                 consec.append(nums.index(0))
#                 nums = nums[nums.index(0)+1::]
#             else:
#                 nums.pop(0)
        
#         if nums:
#             consec.append(len(nums))
        
#         return max(consec)


 
#       ==================== MOST EFFICIENT ====================
        count = 0
        temp = 0
        
        for i in range(len(nums)):
            if i == len(nums)-1 and nums[i]:
                count += 1
                if count > temp:
                    temp = count
                break
                
            if nums[i]:
                count += 1
            else:
                if count > temp:
                    temp = count
                count = 0
                
        return temp


#https://leetcode.com/problems/max-consecutive-ones/