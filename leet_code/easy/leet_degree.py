class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        snums = set(nums)
        degree = max(nums.count(num) for num in snums)
        possible = []
        ignore = set()
        pos_len = []
        
        for num in snums:
            if nums.count(num) == degree:
                possible.append(num)
        
        for p in possible:
            valid = [p]
            numst = list(nums)
            while True:
                if len(numst) == 1:
                    return 1
                temp = list(numst)

                if (temp[0] not in valid and temp[-1] not in valid) or (temp[0] == temp[-1]):
                    ignore.add(temp.pop(0))
                    ignore.add(temp.pop())
                elif temp[0] not in valid or temp[0] in ignore:
                    ignore.add(temp.pop(0))
                    for i in range(len(temp)):
                        if temp[i] not in ignore and temp[i] in valid:
                            temp = temp[i::]
                            break
                else:
                    ignore.add(temp.pop())
                    for i in range(len(temp)-1, -1, -1):
                        if temp[i] not in ignore and temp[i] in valid:
                            temp = temp[:i+1:]
                            break

                if any(temp.count(num) == degree for num in valid):
                    numst = temp
                else:
                    pos_len.append(len(numst))
                    break
        return min(pos_len)

#     jkbielan's answer (very efficient and smart)
#     C = {}
#     for i, n in enumerate(nums):
#         if n in C:
#             C[n].append(i)
#         else:
#             C[n] = [i]
#     M = max([len(i) for i in C.values()])
#     return min([i[-1]-i[0] for i in C.values() if len(i) == M]) + 1


#https://leetcode.com/problems/degree-of-an-array/