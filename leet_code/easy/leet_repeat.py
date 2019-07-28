class Solution:
    def repeatedNTimes(self, A):
        # original solution (inefficient)
        # for i in range(len(A)):
        #     if A.count(A[i]) > 1:
        #         return A[i]
            
        newlist = []
        
        for i in range(len(A)):
            if A[i] not in newlist:
                newlist.append(A[i])
            else:
                return A[i]


#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/