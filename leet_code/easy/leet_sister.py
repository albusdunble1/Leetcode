class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        unique = set(candies)
        
        if len(unique) >= len(candies) / 2:
            return len(candies) / 2
        else:
            return len(unique)
        
#         works but too slow to be accepted
#         sister = []
        
#         for candy in candies:
#             if candy not in sister and len(sister) != len(candies)/2:
#                 if candies.count(candy) >= 1:
#                     sister.append(candy)
#         return len(sister)


#https://leetcode.com/problems/distribute-candies/