class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = str(bin(x)[2:])
        bin_y = str(bin(y)[2:])
        i = 0
        output = 0
        
        if x > y:
            big = bin_x
            small = bin_y     
        else:
            big = bin_y
            small = bin_x

        diff = len(big) - len(small)
        while i < diff:
            small = '0' + small
            i += 1

        for j in range(len(big)):
            if big[j] != small[j]:
                output += 1
        
        return output
            

#https://leetcode.com/problems/hamming-distance/