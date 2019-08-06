class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
#         Original solution (time limit exceeded)
#         output = []
        
        
#         for i in range(len(nums)/2):
#             if i+1 not in nums:
#                 output.append(i+1)
                
#             if len(nums)-i not in nums:
#                 output.append(len(nums)-i)
      
#         if (len(nums)/2+1) not in nums and len(nums) % 2 != 0:       
#             output.append(len(nums)/2+1)
                
#         return output

        array = [num for num in range(1,len(nums)+1)]

        
        return list(set(array) - set(nums))


#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/