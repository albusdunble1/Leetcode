class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        tracker = 0
        start = 0
        
        
        for s in S:
            if s == '(': 
                tracker += 1
                start += 1
            elif s == ')':
                if start > 0:
                    tracker -= 1
                    start -= 1
                else:
                    tracker += 1
        
        return tracker
        

#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/