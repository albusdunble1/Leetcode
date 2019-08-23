class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if not x:
            return 0
        str_x = str(x)
        
        prefix = ''
        
        if str_x[0] == '-':
            prefix = str_x[0]
            str_x = str_x.replace(prefix, '', 1)
        
        output = str_x[::-1]
        
        
        nonzerofound = False
        
        for num in output:
            if num == '0' and not nonzerofound:
                output = output.replace(num, '',1)
            else:
                nonzerofound = True
        
        output = prefix + output
  
        
        if int(output) > 2**31-1 or int(output) < -2**31:
            return 0
        
        return int(output)
    

#https://leetcode.com/problems/reverse-integer/