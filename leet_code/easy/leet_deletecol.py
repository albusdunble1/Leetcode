class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        

        # # refactored solution (more efficient)
        # A2 = zip(*A)
        # output = 0
        
        # for i in range(len(A2)):
        #     if A2[i] != tuple(sorted(A2[i])):
        #         output += 1
        
        # return output


        # original solution (very inefficient)
        A2 = zip(*A)
        
        output = []

        for i in range(len(A2)):
            if A2[i] != tuple(sorted(A2[i])):
                for j in range(len(A2[i])):
                    if A2[i][j] != sorted(A2[i])[j] and i not in output:
                        output.append(i)
                
        
        return len(output)


#https://leetcode.com/problems/delete-columns-to-make-sorted/