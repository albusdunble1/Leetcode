import sys
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        temp = {}
        
        for i in range(len(list1)):
            if list1[i] in list2:
                j = list2.index(list1[i])
                temp[list1[i]] = j+i
        lowest = min(temp.values())      
        
#         original less clean approach

#         for key, val in temp.items():
#             if val == lowest:
#                 output.append(key)

#         return output

        return [key for key,val in temp.items() if val == lowest]

# ==================================================================================================

#         another solution (around the same efficiency)
#         temp = {}
#         output = []
#         smallest = sys.maxsize
        
#         for i in range(len(list1)):
#             if list1[i] in list2:
#                 j = list2.index(list1[i])
#                 temp[list1[i]] = j+i
#                 if i+j < smallest:
#                     temp = {i+j: [list1[i]]}
#                     smallest = i+j
#                 elif i+j == smallest:
#                     temp[i+j].append(list1[i])
        
#         return temp[smallest]
                

#https://leetcode.com/problems/minimum-index-sum-of-two-lists/