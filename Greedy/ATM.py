n = int(input())
m = list(map(int, input().split()))
m.sort()

sum = 0
cnt = len(m)
for i in range(len(m)):
    sum += m[i] * cnt
    cnt -= 1
print(sum)