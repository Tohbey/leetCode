from pip import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordlen = len(word)
        rowBoard, colBoard = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == wordlen:
                return True
            
            if( r<0 or c< 0 or 
               r >= rowBoard or c>=colBoard 
               or word[i] != board[r][c] or
               (r,c) in path):
                return False

            path.add((r,c))
            res = (dfs(r+1,c,i+1) or
                   dfs(r-1,c,i+1) or
                   dfs(r,c+1,i+1) or
                   dfs(r,c-1,i+1))
            
            path.remove((r, c))
            return res
        
        for r in range(rowBoard):
            for c in range(colBoard):
                if dfs(r, c, 0): return True
                
        return False

res = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
res.exist(board, word)