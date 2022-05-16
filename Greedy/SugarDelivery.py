n = int(input())

arr = [5, 3]
cnt = 0
cnt2 = 0

while n > 0:
    for i in range(len(arr)):
        if n % 5 == 0:
            cnt += n // 5
            n = n % 5
        elif n % 3 == 0:
            cnt += n // 3
            n = n % 3
        else:
            cnt2 += n // arr[i]
            n = n % arr[i]
print(min(cnt, cnt2))
