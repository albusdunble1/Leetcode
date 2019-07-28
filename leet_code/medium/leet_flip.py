class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # check rows 
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[i])):
                    if A[i][j]:
                        A[i][j] = 0
                    else:
                        A[i][j] = 1
        
        # check cols
        for i in range(len(A[0])):
            zeroes = 0
            ones = 0
            for j in range(len(A)):
                if A[j][i] == 0:
                    zeroes += 1
                else:
                    ones += 1
            
            if zeroes > ones:
                for j in range(len(A)):
                    if A[j][i]:
                        A[j][i] = 0
                    else:
                        A[j][i] = 1
                        
        # calculate total and convert to int
        sum = 0
        for i in range(len(A)):
            temp = ''.join(str(b) for b in A[i])
            sum += int(temp, 2)
        
        return sum
        

#https://leetcode.com/problems/score-after-flipping-matrix/