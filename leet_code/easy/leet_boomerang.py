class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        
        left = 0
        right = 0
        
        # make sure all points are unique
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        
        # make sure all 3 points do not have the same x or y value
        for i in range(len(points)-1):
            if points[i][0] == points[i+1][0]:
                left += 1
            if points[i][1] == points[i+1][1]:
                right += 1
        
        if left > 1 or right > 1:
            return False
        
        
        # check if x and y increases consistently with a pattern
        ldiff1 = points[1][0] - points[0][0]
        ldiff2 = points[2][0] - points[1][0]
        rdiff1 = points[1][1] - points[0][1]
        rdiff2 = points[2][1] - points[1][1]
        
        # if there is a pattern (it is a straight line)
        if ldiff2 == ldiff1 and rdiff1 == rdiff2:
            return False
        return True


#https://leetcode.com/problems/valid-boomerang/