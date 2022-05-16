n, m = map(int, input().split())
data = list()

for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)

cnt = 0
while(m > 0):
    for i in range(n):
        if data[i] <= m:
            cnt += m // data[i]
            m = m % data[i]
print(cnt)