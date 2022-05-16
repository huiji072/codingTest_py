from itertools import combinations_with_replacement

n = int(input())
data = list(map(int, input().split()))
data.sort()

for i in range(len(data) - 1):
    answer = data[i]