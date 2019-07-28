class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """

        # solution is correct but python doesnt support high number of recursions
    
        # if N == 1 or N == 2:
        #     return 1
        # else:
        #     result = self.fib(N-1) + self.fib(N-2)
        #     return result
        

        # bottoms up solution
        if N == 0:
            return N
        
        
        fibo = [1,1]
        
        if N > 2:
            i = 3
            while True:
                fibo.append(fibo[i-2]+fibo[i-3])
                if i == N:
                    break
                i += 1
                
        return fibo[-1]


#https://leetcode.com/problems/fibonacci-number/