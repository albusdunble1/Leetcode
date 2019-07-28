class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        
        third = []
        
        words = text.split(' ')
        
        for i in range(len(words) - 2):
            if words[i] == first and words[i+1] == second:
                third.append(words[i+2])
                
        return third
    
        # one line solution
        # return [words[i+2] for i in range(len(words) -2 ) if words[i] == first and words[i+1] == second]


#https://leetcode.com/problems/occurrences-after-bigram/

