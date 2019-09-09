# =====================================================================================
# method 3 math logic/two pointer technique (IT WORKS)

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        output = []
        a = 0
        b = 0
        while a < len(A) and b < len(B):
            if B[b][1] > A[a][1]:
                if A[a][1] >= B[b][0] and A[a][0] >= B[b][0]:
                    output.append([A[a][0], A[a][1]])
                elif A[a][1] >= B[b][0] and A[a][0] < B[b][0]:
                    output.append([B[b][0], A[a][1]])
                a += 1
            else:
                if B[b][1] >= A[a][0] and B[b][0] >= A[a][0]:
                    output.append([B[b][0], B[b][1]])
                elif B[b][1] >= A[a][0] and B[b][0] < A[a][0]:
                    output.append([A[a][0], B[b][1]])
                b += 1

        return output

# =====================================================================================
# method 1 brute force (time limit exceeded) (works but very very very inefficient)

# class Solution(object):
#     def intervalIntersection(self, A, B):
#         """
#         :type A: List[List[int]]
#         :type B: List[List[int]]
#         :rtype: List[List[int]]
#         """

#         if not A or not B:
#             return []

#         start = 0
#         flag = False
#         output = []
#         a = 0
#         b = 0
        
        
#         while a < len(A) and b < len(B):
#             # print('loop')
#             # print(output)
#             if B[b][1] > A[a][1]:
#                 # print(str(B[b][1]) + ' > ' + str(A[a][1]))
#                 # print('hi')
#                 for i in range(B[b][0], B[b][1]+1):
#                     if a < len(A):
#                         # print('A[a][0] = ' + str(A[a][0]) + ', A[a][1] = ' + str(A[a][1]))
#                         # print('a = ' + str(a))
#                         # print('i = ' + str(i))
#                         if i in range(A[a][0], A[a][1]+1):
#                             if not flag:
#                                 start = i
#                                 flag = True
#                                 # print('start = ' + str(start))
#                         else:
#                             if flag:
#                                 # print(i)
#                                 output.append([start, i-1])
#                                 # print(output)
#                                 a += 1
#                                 flag = False
#                                 if a < len(A):
#                                     if i in range(A[a][0], A[a][1]+1):
#                                         if not flag:
#                                             start = i
#                                             flag = True
#                                             # print('start = ' + str(start))
#                                 else:
#                                     return output
#                             if A[a][1] < B[b][0]:
#                                 # print('yoi')
#                                 a += 1
#                                 if a < len(A):
#                                     while a < len(A):
#                                         if A[a][1] >= B[b][0]:
#                                             if i in range(A[a][0], A[a][1]+1):
#                                                 if not flag:
#                                                     start = i
#                                                     flag = True
#                                                     # print('start = ' + str(start))
#                                             break
#                                         else:
#                                             # print('lol')
#                                             a += 1
#                         if i == B[b][1]:
#                             if flag:
#                                 # print('yoksajdadasd')
#                                 output.append([start, i])
#                                 # print(output)
#                                 flag = False
#                             b += 1
#                     else:
#                         return output
                        
                        
                    
#             # elif A[a][1] > B[b][1]:
#             else:
#                 # print(str(A[a][1]) + ' > ' + str(B[b][1]))
#                 # print('ho')
#                 for i in range(A[a][0], A[a][1]+1):
#                     if b < len(B):
#                         # print(b)
#                         # print('B[b][0] = ' + str(B[b][0]) + ', B[b][1] = ' + str(B[b][1]))
#                         # print('b = ' + str(b))
#                         if i in range(B[b][0], B[b][1]+1):
#                             if not flag:
#                                 start = i
#                                 flag = True
#                                 # print('start = ' + str(start))
#                         else:
#                             # print('yep')
#                             if flag:
#                                 # print('yo')
#                                 # print(i)
#                                 output.append([start, i-1])
#                                 # print(output)
#                                 b += 1
#                                 flag = False
#                                 if b < len(B):
#                                     if i in range(B[b][0], B[b][1]+1):
#                                         if not flag:
#                                             start = i
#                                             flag = True
#                                             # print('start = ' + str(start))
#                                 else:
#                                     return output
#                             if B[b][1] < A[a][0]:
#                                 # print('yoi')
#                                 b += 1
#                                 if b < len(B):
#                                     while b < len(B):
#                                         if B[b][1] >= A[a][0]:
#                                             if i in range(B[b][0], B[b][1]+1):
#                                                 if not flag:
#                                                     # print('asdasd')
#                                                     start = i
#                                                     flag = True
#                                                     # print('start = ' + str(start))
#                                             break
#                                         else:
#                                             # print('lol')
#                                             b += 1
#                         if i == A[a][1]:
#                             # print('yay')
#                             if flag:
#                                 output.append([start, i])
#                                 # print(output)
#                                 flag = False
#                             a += 1
#                     else:
#                         return output
#         return output

# =====================================================================================
# method 2 using set intersection of ranges (time limit exceeded) (works but generating a range of more than a million numbers takes up too much time)

# class Solution(object):
#     def intervalIntersection(self, A, B):
#         """
#         :type A: List[List[int]]
#         :type B: List[List[int]]
#         :rtype: List[List[int]]
#         """
        
#         list1 = [1,2,3,4,5]
#         list2 = [3,4,5,6,7,8]
        
#         # print(list(set(list2).intersection(set(list1))))
        
#         output = []
#         bdone = True
#         adone = True
#         a = 0
#         b = 0
#         while a < len(A) and b < len(B):
#             # print('a = ' + str(a))
#             # print('b = ' + str(b))
#             if B[b][1] > A[a][1] and bdone and adone:
#                 # print('first')
#                 range1 = range(A[a][0], A[a][1]+1)
#                 range2 = range(B[b][0], B[b][1]+1)
#                 temp = list(set(range1).intersection(set(range2)))
#                 if temp:
#                     output.append([min(temp), max(temp)])
#                     if max(temp) == B[b][1]:
#                         bdone = True
#                     else:
#                         bdone = False
#                 a += 1
#             elif B[b][1] < A[a][1] and adone and bdone:
#                 # print('second')
#                 range2 = range(A[a][0], A[a][1]+1)
#                 range1 = range(B[b][0], B[b][1]+1)
#                 temp = list(set(range1).intersection(set(range2)))
#                 if temp:
#                     output.append([min(temp), max(temp)])
#                     if max(temp) == A[a][1]:
#                         adone = True
#                     else:
#                         adone = False
#                 b += 1
#             elif not bdone:
#                 # print('third')
#                 range1 = range(A[a][0], A[a][1]+1)
#                 range2 = range(B[b][0], B[b][1]+1)
#                 temp = list(set(range1).intersection(set(range2)))
#                 # print(range1)
#                 # print(range2)
#                 if temp:
#                     output.append([min(temp), max(temp)])
#                     if max(temp) == A[a][1]:
#                         # print('hi')
#                         a += 1
                    
#                     if max(temp) == B[b][1]:
#                         bdone = True
#                         b += 1
#                     else:
#                         bdone = False
#                 else:
#                     bdone = True
#                     b += 1
#             elif not adone:
#                 # print('fourth')
#                 range2 = range(A[a][0], A[a][1]+1)
#                 range1 = range(B[b][0], B[b][1]+1)
#                 temp = list(set(range1).intersection(set(range2)))
#                 # print(range1)
#                 # print(range2)
#                 if temp:
#                     if max(temp) == B[b][1]:
#                         b += 1
#                     output.append([min(temp), max(temp)])
#                     if max(temp) == A[a][1]:
#                         adone = True
#                         a += 1
#                     else:
#                         adone = False
#                 else:
#                     adone = True
#                     a += 1
#             # if B[b][1] == A[a][1] 
#             else:
#                 range1 = range(A[a][0], A[a][1]+1)
#                 range2 = range(B[b][0], B[b][1]+1)
#                 temp = list(set(range1).intersection(set(range2)))
#                 if temp:
#                     output.append([min(temp), max(temp)])
#                 a += 1
#                 b += 1
                
#             # print(output)
#         return output



#https://leetcode.com/problems/interval-list-intersections/