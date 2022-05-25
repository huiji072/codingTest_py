n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    # print(v, end=' ')
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
cnt = 0
dfs(graph, 1, visited)
print(cnt-1)