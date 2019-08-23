class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
#       time limit exceeded (correct and original)

        found = False
        start = 0
        end = 0
        highest = 0
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] and not found:
                start = i
                end = i+1
                highest = nums[i]
                found = True
                for j in range(len(nums[:i])):
                    if nums[i+1] < nums[:i][j]:
                        start = j
                        break
            elif nums[i] > nums[i+1] and found:
                end = i+1
                if nums[i] > highest:
                    highest = nums[i]
                for j in range(len(nums[:i])):
                    if nums[i+1] < nums[:i][j]:
                        temp_start = j
                        if temp_start < start:
                            start = temp_start
                        break
               
            elif highest > nums[i+1]:
                end = i+1
        if found:
            return len(nums[start:end+1])
        return 0