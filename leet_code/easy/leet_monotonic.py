class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        increase = False
        neutral = False
        visited = False
        
        for i in range(len(A)-1):
            if not visited and A[i] != A[i+1]:
                if A[i] < A[i+1]:
                    increase = True
                visited = True
            
            if A[i] == A[i+1]:
                neutral = True
            else:
                neutral = False
                
            if not neutral:
                if (increase and A[i] > A[i+1]) or (not increase and A[i] < A[i+1]):
                    return False
        
        return True


#https://leetcode.com/problems/monotonic-array/