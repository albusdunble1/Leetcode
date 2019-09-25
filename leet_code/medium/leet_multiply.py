class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        #extract info for a
        aoperator = a.index('+')
        anum = int(a[:aoperator])
        acoef = int(a[aoperator+1:-1])
        
        #extract info for b
        boperator = b.index('+')
        bnum = int(b[:boperator])
        bcoef = int(b[boperator+1:-1])
        
        # 1st and 2nd part of the format a+bi
        first = 0
        second = 0
        # 1st step (a constant multiply b constant)
        first += anum * bnum
        # 2nd step (a constant multiply b variable)
        second += anum * bcoef
        # 3rd step (a variable multiply b constant)
        second += acoef * bnum
        # 4th step (a variable multiply b variable)
        first += (acoef * bcoef)*-1
        
        output = '{}+{}i'.format(first, second)
        
        return output


#https://leetcode.com/problems/complex-number-multiplication/submissions/