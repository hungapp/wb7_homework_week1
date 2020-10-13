class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def union(x, y):
            x_root, y_root = find(x), find(y)
            if x_root != y_root:
                parents[x_root] = y_root
            
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        if not board:
            return
        r = len(board)
        c = len(board[0])
        parents = list(range(r * c + 1))
        dummy = r*c
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                        union(i*c+j, dummy)
                    else:
                        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            ni, nj = i + x, j + y
                            if board[ni][nj] == 'O':
                                union(i*c+j, ni*c+nj)
        
        for i in range(r):
            for j in range(c):
                if find(i*c+j) == find(dummy):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
