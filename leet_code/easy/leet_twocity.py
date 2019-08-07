class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        list1,list2 = zip(*costs)
        list1 = list(list1)
        list2 = list(list2)
        A = []
        B = []
        ignore = []
        
        while True:
            diff = 0
            for i in range(len(list1)):
                if diff < abs(list1[i]-list2[i]) and i not in ignore:
                    diff = abs(list1[i]-list2[i])
                    diff_i = i
            
            if list1[diff_i] < list2[diff_i] and len(A) != len(costs)/2:
                A.append(list1[diff_i])
                ignore.append(diff_i)
            elif list2[diff_i] < list1[diff_i] and len(B) != len(costs)/2:
                B.append(list2[diff_i])
                ignore.append(diff_i)
            elif len(A) == len(costs)/2:
                for i in range(len(list1)):
                    if i not in ignore:
                        B.append(list2[i])
                break
            elif len(B) == len(costs)/2:
                for i in range(len(list1)):
                    if i not in ignore:
                        A.append(list1[i])
                break
                
        return sum(A) + sum(B)


#https://leetcode.com/problems/two-city-scheduling/