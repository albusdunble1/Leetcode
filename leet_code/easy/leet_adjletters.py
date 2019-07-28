class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        i = 0
        
        while i < len(S) - 1:
            print('loop i = ' + str(i))
            if S[i] == S[i+1]:
                print('before S = ' + S)
                S = S[:i:] + S[i+2::]
                print('after S = ' + S)
                # important
                i = max(0, i-1)
                # important
                print('reset i = ' + str(i))
            else:
                i += 1
        
        return S


#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/