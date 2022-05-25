n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    global cnt
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
cnt = 0
cntlist = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cntlist.append(cnt)
            result += 1
            cnt = 0
print(result)
cntlist.sort()
for i in range(len(cntlist)):
    print(cntlist[i])