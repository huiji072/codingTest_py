T = int(input())

arr = [300, 60, 10]
answer = [0, 0, 0]


for i in range(len(arr)):
    if arr[i] <= T:
        answer[i] = T // arr[i]
        T = T % arr[i]
if T == 0:
    print(answer[0], answer[1], answer[2])
else:
    print(-1)

