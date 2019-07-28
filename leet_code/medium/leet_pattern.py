class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        output = []
        
        pattern_dict = {}
        for p in range(len(pattern)):
            if pattern[p] not in pattern_dict:
                pattern_dict[pattern[p]] = [p]
            else:
                pattern_dict[pattern[p]].append(p)
                
        
        
        temp = []
        for p in range(len(pattern)):
            if pattern[p] not in temp:
                temp.append(pattern[p])
            else:
                temp.remove(pattern[p])
        

        
        for i in range(len(words)):
            temp_word = []
            for j in range(len(words[i])):
                if words[i][j] not in temp_word:
                    temp_word.append(words[i][j])
                else:
                    temp_word.remove(words[i][j])
            if len(temp_word) == len(temp):
                output.append(words[i])

               
        i = 0    
        while i < len(output):
            temp_dict = {}
            for j in range(len(output[i])):
                if output[i][j] not in temp_dict:
                    temp_dict[output[i][j]] = [j]
                else:
                    temp_dict[output[i][j]].append(j)
            
            if len(pattern_dict) == len(temp_dict):
                for j in range(len(output[i])):
                    if pattern_dict[pattern[j]] != temp_dict[output[i][j]]:
            
                        output.pop(i)
                        i -= 1
                        break
            else:
                output.pop(i)
                i -= 1
            
            i += 1
                
        
                        
        return output
                    

#https://leetcode.com/problems/find-and-replace-pattern/


# Thought process
# 1) loop through the letters in 'pattern' and map each letter to its respective index before updating it to 'pattern_dict'
# 2) find the unique letters (letters that appear only once in the word) in 'pattern' and add to 'temp'
# 3) loop through the list of words, locate unique letters in each word, and add it to 'temp_word'
# 4) if the number of unique letters in the selected word (len(temp_word)) is the same as pattern (len(temp)), temporarily add it to 'output'(this is only the first filter)
# 5) loop through 'output' and repeat step 1 (temp_dict instead of pattern_dict)
# 6) compare the length of pattern_dict and temp_dict. 
# 7) If they are not the same, remove the selected word from 'output'
# 8) If they are the same, loop through both dictionaries by using the index of each letter in the selected word (dictionaries aren't ordered), and compare the indices of both dictionaries
# 9) If the indices do not match, remove the selected word from 'output'
                    
                    
                    
                