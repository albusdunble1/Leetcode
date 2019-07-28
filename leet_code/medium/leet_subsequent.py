class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # check if values in s exist in t
        for val in s:
            if val not in t:
                return False
        
        count = 0
        

        
        for i in range(len(t)):
            if t[i] in s and count != len(s):
                if t[i] == s[count]:
                    count += 1


                    
        if count == len(s):
            return True
        else: 
            return False


#https://leetcode.com/problems/is-subsequence/