class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        output = []
        
        for i in range(left, right+1):
            str_i = str(i)
            flag = False
            
            if '0' not in str_i:
                flag = True
                for digit in str_i:
                    if i % int(digit) != 0:
                        flag = False
                        break
                        
            if flag:
                output.append(i)
                
        return output


#https://leetcode.com/problems/self-dividing-numbers/