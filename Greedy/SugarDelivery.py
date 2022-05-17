n = int(input())

arr = [5, 3]

cnt = 0
while n > 2:
    if n % 5 == 0:
        cnt += n // 5
        n = n % 5
    else:
        n -= 3
        cnt += 1
if n == 1 or n == 2:
    print(-1)
else:
    print(cnt)