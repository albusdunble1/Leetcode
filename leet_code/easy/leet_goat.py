class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        array = S.split(' ')
        vowel = 'aeiou'
        
        for i in range(len(array)):
            if array[i][0].lower() in vowel:
                array[i] += 'ma'
            else:
                temp = array[i][0]
                array[i] =  array[i][1::]
                # array[i] =  array[i].replace(array[i][0],'',1) (alternative but slightly slower)
                array[i] += temp + 'ma'
            
            array[i] += 'a'*(i+1)
        
        return ' '.join(array)


#https://leetcode.com/problems/goat-latin/