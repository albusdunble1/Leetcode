class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        
        
        shortest = words[0]
        total = 0
        
        for word in words:
            match = 0
            temp = licensePlate.lower()
            for letter in word:
                if letter in temp:
                    match += 1
                    temp = temp.replace(letter, '',1)
            
            if match > total:
                shortest = word
                total = match
            elif match == total and len(shortest) > len(word):
                shortest = word
        
        return shortest


#https://leetcode.com/problems/shortest-completing-word/