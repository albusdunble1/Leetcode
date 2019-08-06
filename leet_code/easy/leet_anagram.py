class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
            
        for letter in s:
            if letter in t:
                t = t.replace(letter,'',1)
            else:
                return False
        

        return True

        # Solution 2 (Faster)
        # return sorted(s) == sorted(t)


#https://leetcode.com/problems/valid-anagram