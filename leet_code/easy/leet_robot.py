class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
#         vertical = 0
#         horizontal = 0
        
#         for move in moves:
#             if move == 'U':
#                 vertical += 1
#             elif move == 'D':
#                 vertical -= 1
#             elif move == 'L':
#                 horizontal -= 1
#             elif move == 'R':
#                 horizontal += 1
                
#         if not(vertical or horizontal):
#             return True
#         return False

        flag = False

        if 'U' in moves or 'D' in moves:
            if moves.count('U') == moves.count('D'):
                flag = True
            else:
                return False
            
            
        if 'L' in moves or 'R' in moves:
            if moves.count('L') == moves.count('R'):
                flag = True
            else:
                return False
        
        return flag


#https://leetcode.com/problems/robot-return-to-origin/