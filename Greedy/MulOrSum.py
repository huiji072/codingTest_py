s = input()
intS = int(s)
listS = list(map(int, str(intS)))
result = 1
cnt = 0
for i in range(len(listS)):
    if listS[i] == 0:
        result += listS[i]
        cnt += 1
    else:
        result *= listS[i]

if cnt > 0:
    print(result - 1)
else:
    print(result)