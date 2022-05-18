n, m = map(int, input().split())
a, b, d = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

#이미 간 곳은 1로
arr[a][b] = 1
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt = 0
for i in range(n):
    nx = dx[i] + a
    ny = dy[i] + b
    if nx == 1 or ny == 1:
        continue
    cnt += 1
    nx, ny = 1
    a = nx
    b = ny

print(cnt)