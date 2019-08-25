class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        mag_dict = {m:magazine.count(m) for m in set(magazine)}
        
        for r in ransomNote:
            if r in mag_dict:
                mag_dict[r] -= 1
                if mag_dict[r] < 0:
                    return False
            else:
                return False
        
        return True


#https://leetcode.com/problems/ransom-note/