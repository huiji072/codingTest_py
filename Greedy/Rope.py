n = int(input())
k = []
for _ in range(n):
    k.append(int(input()))

k.sort(reverse=True)
temp = []
for i in range(len(k)):
    temp.append(k[i] * (i+1))

print(max(temp))

