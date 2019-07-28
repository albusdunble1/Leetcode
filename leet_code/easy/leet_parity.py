class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
#         youtuber solution

#         front = 0
#         back = len(A) - 1 
        
#         parity_arr= []
        
#         for i in range(len(A)):
#             if A[i] % 2 == 0:
#                 parity_arr.insert(0, A[i])
#             else:
#                 parity_arr.append(A[i])
        
                        
#         return parity_arr

        even = []
        odd = []
        parity_arr = []
        
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
                
        for num in even:
            parity_arr.append(num)
        for num in odd:
            parity_arr.append(num)
            
        return parity_arr


#https://leetcode.com/problems/sort-array-by-parity/