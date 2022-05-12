n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
cnt = 0

for i in range(n) :
    while(sum(data) > 0):
        del data[0:data[i]]
        cnt += 1

print(cnt)