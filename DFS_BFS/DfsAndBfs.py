from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    visited[v] = True
    q = deque([v])
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(v)
visited = [False] * (n+1)
print()
bfs(v)