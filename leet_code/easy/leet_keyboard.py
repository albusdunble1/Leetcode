class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        
        output = []
        absent = False
        temp = ""
        
        for word in words:
            if word[0].lower() in row1:
                temp = row1

            elif word[0].lower() in row2:
                temp = row2
            elif word[0].lower() in row3:
                temp = row3

            for char in word:
                if char.lower() not in temp:
                    absent = True

            if absent == False:
                output.append(word)
            
            absent = False
        
        return output


    #https://leetcode.com/problems/keyboard-row/