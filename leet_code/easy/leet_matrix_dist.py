class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        
        
        matrix = []

        # generate matrix based on R,C
        for i in range(R):
            for j in range(C):
                matrix.append([i,j])

        r = r0
        c = c0

        # bubble sort (O(n^2)) time limit exceeded, but the answer is correct
        # for i in range(0, len(matrix)):
        #     for j in range(0, (len(matrix)-i)-1):
        #         if (abs(r - matrix[j][0]) + abs(c - matrix[j][1])) > (abs(r - matrix[j+1][0]) + abs(c - matrix[j+1][1])):
        #             matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
        
        # sort in a non-decreasing order acording to value x
        matrix.sort(key=lambda x: abs(r-x[0]) + abs(c-x[1]))
                
        return matrix
                    