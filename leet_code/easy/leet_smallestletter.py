class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        tnum = ord(target) - 96
        
        for l in letters:
            if (ord(l)-96) > tnum:
                return l
        
        return letters[0]


#https://leetcode.com/problems/find-smallest-letter-greater-than-target/