#예제 3-1 거스름돈

n = 1260
cnt = 0 #동전개수
arr = [500, 100, 50, 10]

for i in arr:
    cnt += n//i
    n = n % i

print(cnt)

