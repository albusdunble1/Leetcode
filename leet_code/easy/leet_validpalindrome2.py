class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s == s[::-1]:
            return True
        

        possible = []
        
        for i in range(len(s)/2):
            if s[i] != s[len(s)-1-i]:
                possible.extend([i, len(s)-1-i])
                break
        
        
        for i in possible:
            temp_s = list(s)
            temp_s.pop(i)
            if temp_s == temp_s[::-1]:
                return True
        return False

        
#https://leetcode.com/problems/valid-palindrome-ii/