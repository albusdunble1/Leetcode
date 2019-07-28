class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
                
        array = s.split(' ')
        
        if s:
            if len(array[-1]) == 0:
                for i in range(len(array) ,0,-1):
                    if len(array[i-1]) != 0:
                        return len(array[i-1])
            return len(array[-1])
        
        return 0


#https://leetcode.com/problems/length-of-last-word/