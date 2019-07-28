class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        not_letter = {}
        indices = []
        letter = []
        S = list(S)
        
        i = 0
        while i < len(S):
            if not S[i].isalpha():
                not_letter[i] = S[i]
                indices.append(i)
            else:
                letter.append(S[i])
            i += 1
        

        letter.reverse()
        
        for j in range(len(indices)):
            letter.insert(indices[j], not_letter[indices[j]])            
        return ''.join(letter)

#test
#https://leetcode.com/problems/reverse-only-letters/