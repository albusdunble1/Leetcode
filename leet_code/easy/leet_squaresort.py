class Solution:
    def sortedSquares(self, A):
        
        new_list = list(map(lambda x: x * x, A))
        

        # alternative (slightly less efficient)
        # new_list.sort()  
        
        # return new_list
        
        return sorted(new_list)


#https://leetcode.com/problems/squares-of-a-sorted-array/submissions/

