class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s1 = set(s)
        possible = []
        
        for S in s1:
            copy = list(s)
            i = copy.index(S)
            copy.remove(S)
            if set(copy) != s1:
                possible.append(i)
        
        return min(possible) if possible else -1


        # brute force
        # for i in range(len(s)):
        #     if s.count(s[i]) == 1:
        #         return i
        # return -1
        
        
#https://leetcode.com/problems/first-unique-character-in-a-string/