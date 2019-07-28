class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        output = []
        
        small = 0 
        big = len(S)
        
        for i in range(len(S)):
            if S[i] == 'I':
                output.append(small)
                small += 1
            else:
                output.append(big)
                big -= 1
        

        # actually it doesn't matter because in the end, big == small
        if S[len(S)-1] == 'I':
            output.append(big)
        else:
            output.append(small)

        return output


#https://leetcode.com/problems/di-string-match/