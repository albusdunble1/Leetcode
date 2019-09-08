class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dic1 = {}
        dic2 = {}
        
        if not(len(s) == len(t) and len(set(s)) == len(set(t))):
            return False
        
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = [i]
            else:
                dic1[s[i]].append(i)
            
            if t[i] not in dic2:
                dic2[t[i]] = [i]
            else:
                dic2[t[i]].append(i)

        for item in dic1.values():
            if item not in dic2.values():
                return False
        return True


#https://leetcode.com/problems/isomorphic-strings/