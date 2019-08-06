class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if len(str1) == len(str2):
            if str1 != str2:
                return ''
            return str1
        
        
        if len(str1) > len(str2):
            large = str1
            small = str2
        else:
            large = str2
            small = str1
        
        output = ''

        if len(small) % 2 == 0:
            i = 2
        else:
            i = 3

        while i <= len(small):
            temp = large
            temp2 = small
            count = len(large) / i
            count2 = len(small) / i
            
            for j in range(count):
                temp = temp.replace(small[:i:], '',1)
            
            for k in range(count2):
                temp2 = temp2.replace(small[:i:], '',1)
            
            

            if (temp == '' and temp2 == '') and (output == '' or len(small[:i:]) > len(output)):
                output = small[:i:]

            i += 1
            
        return output   


#https://leetcode.com/problems/greatest-common-divisor-of-strings/