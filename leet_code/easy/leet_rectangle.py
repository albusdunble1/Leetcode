class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        

        # correct but time limit exceeded

        if area == 1:
            return [1,1]
        
        for i in range(1, area):
            if area % i == 0:
                diff = abs(area/(area/i) - area/i)
                temp = i
                break
        
        for i in range(temp, area):
            if area % i == 0:
                if abs(area/(area/i) - area/i) < diff:
                    diff = abs(area/(area/i) - area/i)
                    temp = i
        return [max(area/(area/temp),area/temp), min(area/(area/temp),area/temp)]


#https://leetcode.com/problems/construct-the-rectangle/