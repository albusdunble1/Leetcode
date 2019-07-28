def countBattleships(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    
    # num_of_elements = len(board[0])

    # board2 = []

    lr_end, tb_end = False, False

    total = 0


    # rearranging the list according to the columns 

    # for j in range(num_of_elements):
    #     temp_list = []
    #     for i in range(len(board)):
    #         temp_list.append(board[i][j])
    #     board2.append(temp_list)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X':

                if j == len(board[i]) - 1 and i == len(board) - 1:
                    total +=1
                    break

                if j != len(board[i]) - 1:
                    if board[i][j+1] == '.':
                        lr_end = True
                else:
                    lr_end = True



                if i != len(board) - 1:
                    if board[i+1][j] == '.':
                        tb_end = True
                else:
                    tb_end = True

                if lr_end and tb_end:
                    total += 1
                    lr_end = False
                    tb_end = False
                
                lr_end = False
                tb_end = False


    return total

print(countBattleships([
    [".","X",".",".","X"],
    [".","X",".",".","X"],
    [".",".",".",".","X"],
    ["X",".","X","X","."],
    [".",".",".",".","X"]]))


#https://leetcode.com/problems/battleships-in-a-board/