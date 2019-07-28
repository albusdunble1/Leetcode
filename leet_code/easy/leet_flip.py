class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for img in A:
            img.reverse()
            
            for i in range(len(img)):
                if img[i]:
                    img[i] = 0
                else:
                    img[i] = 1

        return A


#=====================================================================================

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        return [[0 if val else 1 for val in img[::-1]] for img in A]


#https://leetcode.com/problems/flipping-an-image/
