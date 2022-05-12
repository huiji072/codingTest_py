n, m, k = map(int, input().split())
data = list(map(int, input().split())) #n개의 수를 공백으로 구분하여 입력받기
sum = 0

data.sort(reverse=True) #내림차순으로 정렬
max = data[0]
min = data[1]

sum += (m % k) * min
sum += (m - (m % k)) * max

print(sum)
