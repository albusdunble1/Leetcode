class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # skyline from left to right
        skyline_lr = [max(grid[i]) for i in range(len(grid))]
        
        
        # skyline from top to bottom
        grid2 = []
        
        num_of_elements = len(grid[0])
        for j in range(num_of_elements):
            temp_list = []
            for i in range(len(grid)):
                temp_list.append(grid[i][j])
            grid2.append(temp_list)
        
        skyline_tb = [max(grid2[i]) for i in range(len(grid2))]
        

        total = 0                     
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if skyline_lr[i] < skyline_tb[j]:
                    temp_min = skyline_lr[i]
                else:
                    temp_min = skyline_tb[j]

                total += (temp_min - grid[i][j])
                grid[i][j] = temp_min

        return total


#https://leetcode.com/problems/max-increase-to-keep-city-skyline/submissions/