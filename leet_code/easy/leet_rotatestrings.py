class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        if not A and not B:
            return True
        elif not A or not B:
            return False
        
        indices =[]
        
        letter = B[0]
        if letter in A:
            for i in range(len(A)):
                if A[i] == letter:
                    indices.append(i)
        else:
            return False

        for i in indices:
            if B == A[i:] + A[:i]:
                return True
        return False
        

#https://leetcode.com/problems/rotate-string/