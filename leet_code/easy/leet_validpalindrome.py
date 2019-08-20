class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = [S for S in s.lower() if S.isalnum()]
        
        # redundant condition statements that i added because i got isalnum() confused with isalpha()

        # if len(s) == 2 and len(set(s)) != 1:
        #     return False
        # if not s:
        #     return True
        
        return s == s[::-1]
            

#https://leetcode.com/problems/valid-palindrome/