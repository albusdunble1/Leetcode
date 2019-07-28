class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        dict_morse = {}
        for i in range(len(morse)):
            dict_morse[alphabets[i]] = morse[i]
        
        
        final_list = []

        
        for word in words:
            temp_str = ""
            for letter in word:
                temp_str += dict_morse[letter]
            final_list.append(temp_str)
        
        return len(set(final_list))


#https://leetcode.com/problems/unique-morse-code-words/