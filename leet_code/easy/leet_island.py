class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        perimeter = 0

        for i in range(len(grid)):
            if len(grid[i]) > 1:
                for j in range(len(grid[i])):
                    left = 0
                    right = 0
                    top = 0
                    bottom = 0
                    if grid[i][j] == 1:
                        if i == 0:
                            top = 1
                            bottom = 1
                            if len(grid) > 1:
                                if grid[i+1][j] == 0:
                                    bottom = 1  
                                else:
                                    bottom = 0
                        elif i == len(grid) - 1:
                            bottom = 1
                            if len(grid) > 1:
                                if grid[i-1][j] == 0:
                                    top = 1
                        else:
                            if grid[i-1][j] == 0:
                                top = 1
                            if grid[i+1][j] == 0:
                                bottom = 1  
                        if j == 0:
                            left = 1
                            if grid[i][j+1] == 0:
                                right = 1
                        elif j == len(grid[i]) - 1:
                            right = 1
                            if grid[i][j-1] == 0:
                                left = 1
                        else:
                            if grid[i][j-1] == 0:
                                left = 1
                            if grid[i][j+1] == 0:
                                right = 1

                    perimeter += (left+right+top+bottom)
            else:
                if len(grid) > 1:
                    left = 0
                    right = 0
                    top = 0
                    bottom = 0
                    if i == 0: 
                        if grid[i][0] == 1:
                            top = 1
                            left = 1
                            right = 1
                            if grid[i+1][0] == 0:
                                    bottom = 1  
                            
                    elif i == len(grid) - 1:
                        if grid[i][0] == 1:
                            bottom = 1
                            left = 1
                            right = 1
                            if grid[i-1][0] == 0:
                                    top = 1  
                    else:
                        if grid[i][0] == 1:
                            left = 1
                            right = 1
                            if grid[i-1][0] == 0:
                                    top = 1
                            if grid[i+1][0] == 0:
                                    bottom = 1 
                            
                    perimeter += (left+right+top+bottom)
                else:
                    if grid[i][0] == 1:
                        return 4
                    else:
                        return 0

        return perimeter


#https://leetcode.com/problems/island-perimeter/