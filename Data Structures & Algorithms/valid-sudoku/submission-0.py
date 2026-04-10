class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = range(9)
        row = []
        col = []
        square = []
        seen = set()

        for i in n:
            for j in n:
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
                    row.append(board[i][j])
            #print(row)
            #print(seen)
            row = []
            seen = set()


        for i in n:
            for j in n:
                if board[j][i] == '.':
                    continue
                else:
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])
                    col.append(board[j][i])
            #print(col)
            #print(seen)
            col = []
            seen = set()
#        for i in range(9):
#            for j in range(9):
#                print((j//3)+3*(i//3), (j%3)+3*(i%3))

        for i in range(9):
            for j in range(9):
                if board[ (j//3)+3*(i//3)][ (j%3)+3*(i%3)] == '.':
                    continue
                else:
                    if board[ (j//3)+3*(i//3)][ (j%3)+3*(i%3)] in seen:
                        return False
                    seen.add(board[ (j//3)+3*(i//3)][ (j%3)+3*(i%3)])
            seen = set()    

        return True
            
            



