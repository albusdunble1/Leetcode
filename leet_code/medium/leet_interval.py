class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # brute force (works but very very very inefficient) (time limit exceeded)

        if not A or not B:
            return []

        start = 0
        flag = False
        output = []
        a = 0
        b = 0
        
        
        while a < len(A) and b < len(B):
            # print('loop')
            # print(output)
            if B[b][1] > A[a][1]:
                # print(str(B[b][1]) + ' > ' + str(A[a][1]))
                # print('hi')
                for i in range(B[b][0], B[b][1]+1):
                    if a < len(A):
                        # print('A[a][0] = ' + str(A[a][0]) + ', A[a][1] = ' + str(A[a][1]))
                        # print('a = ' + str(a))
                        # print('i = ' + str(i))
                        if i in range(A[a][0], A[a][1]+1):
                            if not flag:
                                start = i
                                flag = True
                                # print('start = ' + str(start))
                        else:
                            if flag:
                                # print(i)
                                output.append([start, i-1])
                                # print(output)
                                a += 1
                                flag = False
                                if a < len(A):
                                    if i in range(A[a][0], A[a][1]+1):
                                        if not flag:
                                            start = i
                                            flag = True
                                            # print('start = ' + str(start))
                                else:
                                    return output
                            if A[a][1] < B[b][0]:
                                # print('yoi')
                                a += 1
                                if a < len(A):
                                    while a < len(A):
                                        if A[a][1] >= B[b][0]:
                                            if i in range(A[a][0], A[a][1]+1):
                                                if not flag:
                                                    start = i
                                                    flag = True
                                                    # print('start = ' + str(start))
                                            break
                                        else:
                                            # print('lol')
                                            a += 1
                        if i == B[b][1]:
                            if flag:
                                # print('yoksajdadasd')
                                output.append([start, i])
                                # print(output)
                                flag = False
                            b += 1
                    else:
                        return output
                        
                        
                    
            # elif A[a][1] > B[b][1]:
            else:
                # print(str(A[a][1]) + ' > ' + str(B[b][1]))
                # print('ho')
                for i in range(A[a][0], A[a][1]+1):
                    if b < len(B):
                        # print(b)
                        # print('B[b][0] = ' + str(B[b][0]) + ', B[b][1] = ' + str(B[b][1]))
                        # print('b = ' + str(b))
                        if i in range(B[b][0], B[b][1]+1):
                            if not flag:
                                start = i
                                flag = True
                                # print('start = ' + str(start))
                        else:
                            # print('yep')
                            if flag:
                                # print('yo')
                                # print(i)
                                output.append([start, i-1])
                                # print(output)
                                b += 1
                                flag = False
                                if b < len(B):
                                    if i in range(B[b][0], B[b][1]+1):
                                        if not flag:
                                            start = i
                                            flag = True
                                            # print('start = ' + str(start))
                                else:
                                    return output
                            if B[b][1] < A[a][0]:
                                # print('yoi')
                                b += 1
                                if b < len(B):
                                    while b < len(B):
                                        if B[b][1] >= A[a][0]:
                                            if i in range(B[b][0], B[b][1]+1):
                                                if not flag:
                                                    # print('asdasd')
                                                    start = i
                                                    flag = True
                                                    # print('start = ' + str(start))
                                            break
                                        else:
                                            # print('lol')
                                            b += 1
                        if i == A[a][1]:
                            # print('yay')
                            if flag:
                                output.append([start, i])
                                # print(output)
                                flag = False
                            a += 1
                    else:
                        return output
        return output


#https://leetcode.com/problems/interval-list-intersections/