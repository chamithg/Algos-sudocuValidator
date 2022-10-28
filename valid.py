
import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        subSqures = collections.defaultdict(set)   ## here key shold represent 9 small suqares (AB)
        ## if coll/row no <3  A ; 3<coll/row no <6  B ; 6<coll/row no   c
        
        for r in range(9):
            if r < 3:
                rId = "A"
            elif r >= 3 and r < 6:
                rId = "B"
            else:
                rId = "C"
                    
            
            for c in range(9):
                
                if c < 3:
                    cId = "A"
                elif c >= 3 and c < 6:
                    cId = "B"
                else:
                    cId = "C"
                    
                print(r,c,rId,cId)
                if board[r][c] ==".":
                    continue
                if (board[r][c] in cols[c] or 
                    board[r][c] in rows[r] or 
                    board[r][c] in subSqures[ rId+cId]):
                    return False
                print(board[r][c])
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                subSqures[rId+cId].add(board[r][c])
        print(subSqures)
        return True   
         



board = [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]




check = Solution()

print(check.isValidSudoku(board))
