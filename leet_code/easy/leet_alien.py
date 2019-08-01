class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        # index of the letter to be compared
        l = 0
        
        for i in range(len(words)-1):
            # compare the indices of the first letter of the 2 words
            if order.index(words[i][l]) > order.index(words[i+1][l]):
                return False
            # if they are the same, compare the next letter and so on with while loop
            elif order.index(words[i][l]) == order.index(words[i+1][l]):
                l += 1
                while l < min(len(words[i]), len(words[i+1])):
                    if order.index(words[i][l]) > order.index(words[i+1][l]):
                        return False
                    l += 1
                
                # if nothing is resolved from the loop, check for the longer word
                if len(words[i]) > len(words[i+1]):
                    return False
        
        # if all the checks are bypassed, that means it's sorted
        return True


#https://leetcode.com/problems/verifying-an-alien-dictionary/