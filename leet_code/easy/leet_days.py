class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        
        small = [4,6,9,11]
        
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        output = 0
        
        if year % 4 != 0:
            feb = 28
        elif year % 100 != 0:
            feb = 29
        elif year % 400 != 0:
            feb = 28
        else:
            feb = 29

        for i in range(month-1):
            if i+1 == 2:
                output += feb
            elif i+1 in small:
                output += 30
            else:
                output += 31
        
        return output + day
                

#https://leetcode.com/problems/day-of-the-year/