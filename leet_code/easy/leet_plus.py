class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits = [str(d) for d in digits]
        
        string = ''.join(digits)
        integer = int(string)+1
        return list(str(integer))


#https://leetcode.com/problems/plus-one/