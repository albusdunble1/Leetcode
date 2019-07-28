class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = [1,1]
        
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            for i in range(2, rowIndex+1):
                count = 0
                temp_arr = []
                
                for k in range(i+1):
                    if k == 0 or k == i:
                        temp_arr.append(1)
                        # print("temp_ar: " + str(temp_arr) + ", i: " + str(i))
                    else:
                        temp_arr.append(pascal[count] + pascal[count+1])
                        # print("pascal[count] + pascal[count+1] = " + str(pascal[count] + pascal[count+1]))
                        # print("temp_ar: " + str(temp_arr) + ", count: " + str(count) + ", i: " + str(i))
                        count += 1

                pascal = temp_arr
    
        return pascal


#https://leetcode.com/problems/pascals-triangle-ii/
