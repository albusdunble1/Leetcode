class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # x = i
        # y = j
        # z = grid[i][j]
        # always a cube
        
        # top view
        xy_area = 0
        
        #side view
        yz_area = 0
        
        #front view
        xz_area = 0
        
        total_area = 0


        # refactored version
        
        # if len(grid) > 1:
        #     # top view 
        #     for x in range(len(grid)):
        #         biggest_in_row = 0
        #         biggest_in_col = 0
        #         for y in range(len(grid[x])):
        #             if grid[x][y] != 0:
        #                 xy_area += 1
                        
        #             if biggest_in_row < grid[x][y]:
        #                 biggest_in_row = grid[x][y]
                        
        #             if biggest_in_col < grid[y][x]:
        #                 biggest_in_col = grid[y][x]
                    
        #         yz_area += biggest_in_row
        #         xz_area += biggest_in_col  
        
        if len(grid) > 1:
            # top view 
            for x in grid:
                for y in x:
                    if y != 0:
                        xy_area += 1
            
            #side view
            for x in range(len(grid)):
                biggest_in_row = 0
                for y in range(len(grid[x])):
                    if biggest_in_row < grid[x][y]:
                        biggest_in_row = grid[x][y]

                    
                # print("row biggest = " + str(biggest_in_row))    
                yz_area += biggest_in_row
            
            #front view
            for x in range(len(grid)):
                biggest_in_col = 0
                for y in range(len(grid[x])):
                    if biggest_in_col < grid[y][x]:
                        biggest_in_col = grid[y][x]
                    
                xz_area += biggest_in_col   
                # print("col biggest = " + str(biggest_in_col))    
            
                        
            
        else:
            # top view
            xy_area = 1
            yz_area = grid[0][0]
            xz_area = grid[0][0]
            
        

        # print(xy_area)
        # print(yz_area)
        # print(xz_area)
        total_area = xy_area + yz_area + xz_area
            
        
                    
        return total_area


#https://leetcode.com/problems/projection-area-of-3d-shapes/