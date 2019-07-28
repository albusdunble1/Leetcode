class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        temp = s.split(' ')
        
        output = [word[::-1] for word in temp]
        
        return " ".join(output)


#https://leetcode.com/problems/reverse-words-in-a-string-iii/