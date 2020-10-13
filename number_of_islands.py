class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        row_num, col_num = len(grid), len(grid[0])
        parent = [i for i in range(row_num * col_num)]
        self.count = sum(grid[i][j] == '1' for j in range(col_num) for i in range(row_num))
        
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
                
        def union(x, y):
            x_root, y_root = find(x), find(y)
            if x_root == y_root: return
            parent[x_root] = y_root
            self.count -= 1
        
        
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == '0':
                    continue
                index = i * col_num + j
                if j < col_num - 1 and grid[i][j + 1] == '1':
                    union(index, index + 1)
                if i < row_num - 1 and grid[i + 1][j] == '1':
                    union(index, index + col_num)
        return self.count
