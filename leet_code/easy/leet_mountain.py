class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # return A.index(max(A))
        
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                return i
            

#https://leetcode.com/problems/peak-index-in-a-mountain-array/