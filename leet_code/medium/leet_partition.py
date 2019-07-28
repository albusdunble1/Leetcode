class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        
        output = []
        seen = []
        temp = ''
        
        i = 0
        while i < len(S):
            # the first occurence
            if i == S.index(S[i]) and S[i] not in seen:
                if not temp:
                    temp = S[i]
                else:
                    if S.rfind(temp) < S.rfind(S[i]):
                        temp = S[i]
                seen.append(S[i]) 
            
            # the last occurence
            if i == S.rfind(temp):
                output.append(len(S[:i+1:]))
                S = S[i+1::] 
                i = 0
                temp = ''
            else:
                i += 1
            
        return output


#https://leetcode.com/problems/partition-labels/