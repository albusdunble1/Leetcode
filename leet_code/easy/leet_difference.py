class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
                
        for T in t:
            if T not in s:
                return T
            s = s.replace(T, '',1)


#https://leetcode.com/problems/find-the-difference/