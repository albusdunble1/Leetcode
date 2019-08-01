class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        temp = []
        T = list(T)
        
        for s in S:
            while s in T:
                temp.append(T.pop(T.index(s)))
        
        return ''.join(temp) + ''.join(T)
                

#https://leetcode.com/problems/custom-sort-string/