class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        arr = sorted(nums, reverse = True)
        result = {}
        
        for i in range(0, len(nums)):
            if i == 0:
                result[arr[i]] = "Gold Medal"
            elif i == 1:
                result[arr[i]] = "Silver Medal"
            elif i == 2:
                result[arr[i]] = "Bronze Medal"
            else:
                result[arr[i]] = str(i+1)
        
        return list(map(lambda x: result[x], nums))


#https://leetcode.com/problems/relative-ranks/