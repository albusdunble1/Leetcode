class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        # find booked seats
        booked = []
        maxzero = 0
        start_found = 0
        start = 0
        maxzero_index = []
        count = 0  
        before_one = False
        after_one = False
        startwzero = False
        startwzero_index = []
        result2 = 0
        
        if seats[0] == 0:
            startwzero = True
        
        
        for i in range(len(seats)):
            if seats[i] == 1:
                booked.append(i)       
                if startwzero:
                    startwzero_index = [0,i-1]
                    startwzero = False
                
                if count > maxzero:
                    maxzero = count
                    maxzero_index = [start, i-1]
                    before_one = True
                count = 0
                start_found = False
            elif i == len(seats)-1 and seats[i] == 0:
                if not start_found:
                    start = i
                count += 1
                if count >= maxzero-1:
                    maxzero = count
                    maxzero_index = [start, i]
                    before_one = False
            else:
                if not start_found:
                    start_found = True
                    start = i
                count += 1

        
        
        if maxzero_index[0] - 1 >= 0:
            after_one = True
            
        if before_one and after_one:
            if sum(maxzero_index) < 2:
                result = (maxzero_index[1]+1) - maxzero_index[0]
            result = (sum(maxzero_index) / 2) - (maxzero_index[0]-1) 
        elif before_one and not after_one:
            if sum(maxzero_index) < 2:
                result = (maxzero_index[1]+1) - maxzero_index[0]
            result = (maxzero_index[1]+1) - maxzero_index[0]
        else:
            result = maxzero_index[1] - (maxzero_index[0]-1)
        
        
        if startwzero_index:
            result2 = startwzero_index[1] - startwzero_index[0] + 1
        
        if result > result2:
            return result
        return result2
        

#https://leetcode.com/problems/maximize-distance-to-closest-person/