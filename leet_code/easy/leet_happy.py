class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        found = []
        
        while True:
            sn = str(n)
            n = 0
            for num in sn:
                n += int(num) ** 2
            
            if n in found:
                return False
        
            if n == 1:
                return True
            else:
                found.append(n)


#https://leetcode.com/problems/happy-number/