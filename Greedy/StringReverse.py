s = input()
cnt0 = 0 #전부 0으로 바꾸는 경우
cnt1 =1 #전부 1로 바꾸는 경우

for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        if s[i] == '1':
            cnt0 += 1
        else:
            cnt1 += 1

answer = min(cnt0, cnt1)
print(answer)