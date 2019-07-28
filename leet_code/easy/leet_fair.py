class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        atotal = sum(A)
        btotal = sum(B)
        
        if atotal == btotal:
            return [A[0],A[0]]
        
        compromise = int((atotal + btotal) / 2)
        # print(compromise)
        
        if len(B) > 1 and len(A) > 1:
            for i in range(int(len(B)/2)+1):
                # print('B')
                for j in range(int(len(A)/2)):
                    # print('A')
                    if btotal - B[i] + A[j] == compromise and atotal - A[j] + B[i] == compromise:
                        return [A[j],B[i]]
                    if btotal - B[len(B) - (i+1)] + A[len(A) - (j+1)] == compromise and atotal - A[len(A) - (j+1)] + B[len(B) - (i+1)] == compromise:
                        return [A[len(A) - (j+1)],B[len(B) - (i+1)]]
                    
                    
                    
                    if btotal - B[i] + A[len(A) - (j+1)] == compromise and atotal - A[len(A) - (j+1)] + B[i] == compromise:
                        return [A[len(A) - (j+1)],B[i]]
                    if btotal - B[len(B) - (i+1)] + A[j] == compromise and atotal - A[j] + B[len(B) - (i+1)] == compromise:
                        return [A[j],B[len(B) - (i+1)]]
                    
            #check the middle one if it's odd
            middle = A[int(len(A)/2)]
            # print(middle)
            for i in range(len(B)):
                if btotal - B[i] + middle == compromise and atotal - middle + B[i] == compromise:
                    return [middle, B[i]]
                
        else:
            for i in range(len(B)):
                for j in range(len(A)):
                    if btotal - B[i] + A[j] == compromise and atotal - A[j] + B[i] == compromise:
                        return [A[j],B[i]]


#https://leetcode.com/problems/fair-candy-swap/