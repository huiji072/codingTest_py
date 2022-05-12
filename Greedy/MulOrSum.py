s = input()
intS = int(s)
listS = list(map(int, str(intS)))
result = 1
cnt = 0
for i in range(len(listS)):
    if listS[i] == 0:
        result += listS[i]
        cnt += 1 #처음에 0이면 곱셈을 해도 0이 나오니 0을 한번이라도 있다면 1을 증가시키고
    else:
        result *= listS[i]

if cnt > 0:
    print(result - 1) #1이 증가되있다면 최종값에서 -1을 해서 result = 0인것처럼한다.
else:
    print(result)