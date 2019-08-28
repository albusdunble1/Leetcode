class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
 
        for i in range(1,len(s)+1):
            if len(s) % i == 0 and len(s) / i != 1:
                multiply = len(s) / i
                if (s[:i]*multiply) == s:
                    return True

        return False


#https://leetcode.com/problems/repeated-substring-pattern/