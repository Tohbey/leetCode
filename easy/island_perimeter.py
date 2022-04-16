from pip import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c]==0 or (r,c) in visit: 
                return 1
            visit.add((r,c))
            for new_r, new_c in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if (new_r,new_c) not in visit:
                    check=dfs(new_r,new_c)
                    if check:
                        self.res+=check 
        self.res=0
        visit=set()
        ROWS,COLS=len(grid),len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    dfs(i,j)
        
        return self.res


res = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
res.islandPerimeter(grid)