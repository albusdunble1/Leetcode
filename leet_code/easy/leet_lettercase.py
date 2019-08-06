class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if len(word) < 2:
            return True
        
        if word[0] == word[0].upper() and word[1] == word[1].upper():
            for i in range(2,len(word)):
                if word[i] != word[i].upper():
                    return False
        elif word[0] == word[0].upper() and word[1] != word[1].upper():
            for i in range(2,len(word)):
                if word[i] != word[i].lower():
                    return False
        elif word[0] != word[0].upper():
            for i in range(1,len(word)):
                if word[i] != word[i].lower():
                    return False
        
        return True


#https://leetcode.com/problems/detect-capital/