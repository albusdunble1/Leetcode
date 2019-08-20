class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        set_s = set(s)
        output = 0
        one = False
        
        if all(True if s.count(ss) % 2 == 0 else False for ss in set_s):
            return len(s)

        for ss in set_s:
            if s.count(ss) == 1 and not one:
                output += 1
                one = True
            else:
                if s.count(ss) % 2 == 0:
                    output += s.count(ss)
                else:
                    output += s.count(ss) - 1
        
        if not one:
            output += 1
        
        return output


#https://leetcode.com/problems/longest-palindrome/