n, m, k, x = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(i, j):
    if i < 0 or j < 0 or i > n or j > n:
        return False
    if graph[i][j] == x:
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        return True
    return False

