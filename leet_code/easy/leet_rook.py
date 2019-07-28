class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        rx = 0
        ry = 0
        output = 0
        
        # find the indices of Rook
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    rx = i
                    ry = j
                    break

        # check upper
        for x in range(rx-1, 0 ,-1):
            if board[x][ry] == 'B':
                break
            elif board[x][ry] == 'p':
                output += 1
                break
        
        # check lower
        for x in range(rx+1, len(board)):
            if board[x][ry] == 'B':
                break
            elif board[x][ry] == 'p':
                output += 1
                break
                
        # check left
        for y in range(ry-1, 0, -1):
            if board[rx][y] == 'B':
                break
            elif board[rx][y] == 'p':
                output += 1
                break
                
        # check right
        for y in range(ry+1, len(board)):
            if board[rx][y] == 'B':
                break
            elif board[rx][y] == 'p':
                output += 1
                break
        
        return output


#https://leetcode.com/problems/available-captures-for-rook/