class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        
        temp = S[0]
        count = 1
        start = 0
        output = []
        
        for i in range(1,len(S)):
            if S[i] == temp:
                count += 1
            else:
                if count > 2:
                    output.append([start, i-1])
                temp = S[i]
                count = 1
                start = i
            
            if i == len(S) - 1 and count > 2:
                output.append([start, i])
            
        return output
                

#https://leetcode.com/problems/positions-of-large-groups/