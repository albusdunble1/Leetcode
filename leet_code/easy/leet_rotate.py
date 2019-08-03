class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        invalid = ['3','4','7']
        special = ['2','5','6','9']

        output = 0
        
        for i in range(N):
            v_found = False
            for num in str(i+1):
                if num in invalid:
                    v_found = False
                    break
                elif num in special:
                    v_found = True 
            if v_found:
                output += 1
            
                    
        return output


#https://leetcode.com/problems/rotated-digits/