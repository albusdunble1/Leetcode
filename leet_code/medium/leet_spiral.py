class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        
        x = 1
        y = 1
        up = False
        left = False
        output = [[r0,c0]]
        movex = True
        
        while True:
            if movex:
                if not left:
                    # print('right: ' + str(x))
                    for i in range(x):
                        c0 += 1
                        # print(c0)
                        if len(output) < R*C:
                            if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                                output.append([r0,c0])
                                # print(output)
                        else:
                            return output
                    left = True
                else:
                    # print('left: ' + str(x))
                    for i in range(x):
                        c0 -= 1
                        # print(c0)
                        if len(output) < R*C:
                            if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                                output.append([r0,c0])
                                # print(output)
                        else:
                            return output
                    left = False
                movex = False
                x += 1
            else:
                if not up:
                    # print('down')
                    for i in range(y):
                        r0 += 1
                        if len(output) < R*C:
                            if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                                output.append([r0,c0])
                                # print(output)
                        else:
                            return output
                    up = True
                else:
                    # print('up')
                    for i in range(y):
                        r0 -= 1
                        if len(output) < R*C:
                            if r0 >= 0 and r0 < R and c0 >= 0 and c0 < C:
                                output.append([r0,c0])
                                # print(output)
                        else:
                            return output
                    up = False
                movex = True
                y += 1
         
        return output


#https://leetcode.com/problems/spiral-matrix-iii/