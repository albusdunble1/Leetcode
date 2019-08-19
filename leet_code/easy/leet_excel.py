class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        output = 0
        for i in range(len(s)-1,-1, -1):
            output += (ord(s[i].lower())-96)*(26**count)
            count += 1
            
        return output
            

#https://leetcode.com/problems/excel-sheet-column-number/