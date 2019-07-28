class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        special = 'IXC'
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        
        i = 0
        while i < len(s):
            if s[i] not in special:
                total += roman[s[i]]
                
            else:
                if i != len(s)-1:
                    if s[i] == 'I':
                        if s[i+1] == 'V' or s[i+1] == 'X':
                            total += (roman[s[i+1]]-roman[s[i]])
                            i += 1
                        else:
                            total += roman[s[i]]
                    elif s[i] == 'X':
                        if s[i+1] == 'L' or s[i+1] == 'C':
                            total += (roman[s[i+1]]-roman[s[i]])
                            i += 1
                        else:
                            total += roman[s[i]]
                    else:
                        if s[i+1] == 'D' or s[i+1] == 'M':
                            total += (roman[s[i+1]]-roman[s[i]])
                            i += 1
                        else:
                            total += roman[s[i]]
                else:
                    total += roman[s[i]]
            
            i += 1
        
        return total


#https://leetcode.com/problems/roman-to-integer/