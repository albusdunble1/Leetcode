class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
#         original solution

#         B = []

#         find index of smallest val
#         smallest = A.index(min(A))
        
#         ref = A[smallest] + K 
#         B.append(ref)
        
#         for i in range(len(A)):
#             # if i != smallest:
#             if A[i] > ref:
#                 temp = A[i] - ref
#                 if temp < K:
#                     A[i] -= temp
#                 else:
#                     A[i] -= K

#             elif A[i] < ref:
#                 temp = ref - A[i]
#                 if temp < K:
#                     A[i] += temp
#                 else:
#                     A[i] += K


#             B.append(A[i]) 
        
#         return max(B) - min(B)






#         second solution

#         sortedA = sorted(A)
#         sortedA[0] += K
#         last = len(sortedA)-1
        
#         if sortedA[last] != sortedA[0]:
#             temp = sortedA[last] - sortedA[0]
#             if temp < K:
#                 return 0
#             else:
#                 sortedA[last] -= K
#                 return sortedA[last] - sortedA[0]
#         else:
#             return 0





#       second solution refactored

        # first = min(A) + K
        # last = max(A)
        
        # temp = last - first
        # if temp < K:
        #     return 0
        # else:
        #     last -= K
        #     return last - first
        # return 0


#       second solution with more refactoring
        first = min(A) + K
        last = max(A)
        
        temp = last - first
        if temp > K:
            return last - K - first
        return 0


#https://leetcode.com/problems/smallest-range-i/