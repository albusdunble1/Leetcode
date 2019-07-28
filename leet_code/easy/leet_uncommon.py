class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        Al = A.split(' ')
        Bl = B.split(' ')
        
        output = []
        delete = []

        
        if len(Al) > len(Bl):
            bigger = Al
            smaller = Bl
        else:
            bigger = Bl
            smaller = Al
            
        output.extend(bigger)
        output.extend(smaller)
        for i in range(len(bigger)):
            if (bigger.count(bigger[i]) > 1 or bigger[i] in smaller) and bigger[i] not in delete:
                delete.append(bigger[i])
        
        for i in range(len(smaller)):
            if smaller.count(smaller[i]) > 1 and smaller[i] not in delete:
                delete.append(smaller[i])
                
        j = 0
        while j < len(output):
            if output[j] in delete:
                output.pop(j)
                j -= 1
            j += 1
        
        return output


#         other solution, not mine (very efficient)
#         real_output = []
#         for val in output:
#             if output.count(val) == 1:
#                 real_output.append(val)
        
#         return real_output


#https://leetcode.com/problems/uncommon-words-from-two-sentences/