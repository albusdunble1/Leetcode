class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        pairs = {}
        
        for i in range(len(numbers)):
            if target - numbers[i] not in pairs.keys():
                pairs[numbers[i]] = i
            else:
                return [pairs[target - numbers[i]]+1, i+1]


#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/