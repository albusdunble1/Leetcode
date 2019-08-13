class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        fives = 0
        tens = 0
        
        for i in range(len(bills)):
            if bills[i] == 5:
                fives += 1
            elif bills[i] == 10:
                tens += 1
                fives -= 1
            else:
                if tens and fives:
                    fives -= 1
                    tens -= 1
                else:
                    fives -= 3

            if fives < 0:
                return False

        return True
            

#https://leetcode.com/problems/lemonade-change/