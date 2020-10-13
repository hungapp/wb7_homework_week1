class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def find(node):
            if circles[node] == node:
                return node
            root = find(circles[node])
            circles[node] = root
            return root
            
        
        circles = {i: i for i in range(len(M))}
        for i in range(len(M)):
            for j in range(i, len(M)):
                if i != j and M[i][j] == 1 and find(i) != find(j):
                    circles[find(i)] = find(j)
        
        return sum([1 for key, value in circles.items() if key == value])
    # return a total number of roots
