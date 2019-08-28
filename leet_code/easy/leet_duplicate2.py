class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        found = {}
        
        
        for i in range(len(nums)):
            if nums[i] not in found:
                found[nums[i]] = [i]
            else:
                valid = [i-(j+1) for j in range(k)]
                for v in valid:
                    if v in found[nums[i]]:
                        return True
                found[nums[i]].append(i)
                
        return False


#https://leetcode.com/problems/contains-duplicate-ii/