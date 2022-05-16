from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

com = list(combinations(data, 2))

cnt = len(com)
for i in range(len(com)):
    temp = com[i]
    if temp[0] == temp[1]:
        cnt -= 1

print(cnt)
