class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        leap = 2*k
        
        s = list(s)
        for i in range(0,len(s),leap):
            # original solution
            # s = s[:i:]+ s[i:i+k:][::-1] + s[i+k:]
            s[i:i+k:] = s[i:i+k:][::-1]

        return ''.join(s)


#https://leetcode.com/problems/reverse-string-ii/