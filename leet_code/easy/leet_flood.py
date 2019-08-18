class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
#         original answer   
#      
#         def fill(image, sr, sc, newColor, starting_color):
#             starting_color = image[sr][sc]
#             modified = list(image)
#             modified[sr][sc] = newColor
#             # up
#             if sr - 1 >= 0 and modified[sr-1][sc] != newColor and modified[sr-1][sc] == starting_color:
#                 modified = fill(modified, sr-1, sc, newColor, starting_color)
#             # down
#             if sr + 1 < len(image) and modified[sr+1][sc] != newColor and modified[sr+1][sc] == starting_color:
#                 modified = fill(modified, sr+1, sc, newColor, starting_color)
#             # left
#             if sc - 1 >= 0 and modified[sr][sc-1] != newColor and modified[sr][sc-1] == starting_color:
#                 modified = fill(modified, sr, sc-1, newColor, starting_color)
#             #right
#             if sc + 1 < len(image[sr]) and modified[sr][sc+1] != newColor and modified[sr][sc+1] == starting_color:
#                 modified = fill(modified, sr, sc+1, newColor, starting_color)

#             return modified
        
#         return fill(image, sr, sc, newColor, image[sr][sc])




#       refactored answer 

        starting_color = image[sr][sc]
        def fill(image, sr, sc, newColor):
            image[sr][sc] = newColor
            
            # up
            if sr - 1 >= 0 and image[sr-1][sc] != newColor and image[sr-1][sc] == starting_color:
                image = fill(image, sr-1, sc, newColor)
            # down
            if sr + 1 < len(image) and image[sr+1][sc] != newColor and image[sr+1][sc] == starting_color:
                image = fill(image, sr+1, sc, newColor)
            # left
            if sc - 1 >= 0 and image[sr][sc-1] != newColor and image[sr][sc-1] == starting_color:
                image = fill(image, sr, sc-1, newColor)
            #right
            if sc + 1 < len(image[sr]) and image[sr][sc+1] != newColor and image[sr][sc+1] == starting_color:
                image = fill(image, sr, sc+1, newColor)

            return image
        
        fill(image, sr, sc, newColor)
        return image


#https://leetcode.com/problems/flood-fill/