class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        A = list(A)
        B = list(B)
        
        if len(A) != len(B) or (A == B and len(set(A)) == len(A)) or set(A) != set(B):
            return False
        elif A == B and len(set(A)) != len(A):
            return True
        
        for i in range(len(A)):
            if A[i] != B[i]:
                if i == len(A)-1:
                    return False
                for j in range(i+1,len(A)):
                    if A[j] != B[j]:
                        A[i], A[j] = A[j], A[i]
                        
                        return A == B
                

#https://leetcode.com/problems/buddy-strings/