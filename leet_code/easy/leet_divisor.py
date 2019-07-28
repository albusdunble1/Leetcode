class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        
        # choose a number x
        # x must be a multiple of N
        # replace N with N-x
        # return true if Alice wins
        # Alice starts first
         
        
        if N < 2:
            return False
        elif N < 3:
            # Alice wins, because N=2 and only 1 can be chosen
            return True
        
        
        alice = 0
        bob = 0
    
        i = 1
        while i < N:
            print("i = " + str(i) + ", N = " + str(N))
            if N % i == 0:
                if alice > bob:
                    # bob's turn
                    bob += 1
                    N -= i
                    print('Bob chose ' + str(i))
                    i = 0
                    print('Bob turn N = ' + str(N))
                else:
                    # alice's turn
                    alice += 1
                    N -= i
                    print('Alice chose ' + str(i))
                    i = 0
                    print('Alice turn N = ' + str(N))
            i += 1
                    
    
        print('\n\nalice = ' + str(alice))
        print('bob = ' + str(bob))
        return alice > bob


#https://leetcode.com/problems/divisor-game/