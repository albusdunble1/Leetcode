class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        
        for nums in A:
            if nums % 2 == 0:
                even.append(nums)
            else:
                odd.append(nums)
                
        # [even.append(nums) if nums % 2 == 0 else odd.append(nums) for nums in A] (alternative using list comprehension)

        for i in range(len(A)):  
            if i % 2 == 0:
                A[i] = even.pop()
            else:
                A[i] = odd.pop()

        return A
    
#         SOLUTION 2 (inefficient)
#         ans_list = []
        
#         a_length = len(A)


#         for i in range(a_length):
#             j = 0
#             if i % 2 == 0: 
#                 while True:
#                     if A[j] % 2 == 0:
#                         ans_list.append(A.pop(j))
#                         break
#                     j += 1
#             else:
#                 while True:
#                     if A[j] % 2 != 0:
#                         ans_list.append(A.pop(j))
#                         break
#                     j += 1
            
#         return ans_list


#https://leetcode.com/problems/sort-array-by-parity-ii/