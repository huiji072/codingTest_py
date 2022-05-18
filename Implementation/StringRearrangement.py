import re
from string import digits

s = input()

# 숫자만 추출
numbers = re.findall(r'\d', s)
# 숫자의 합
sum = 0
for i in range(len(numbers)):
    sum += int(numbers[i])
sum = str(sum)
# 숫자만 제거
str = re.sub(r'[0-9]+', '', s)
str = list(str)

# 오름차순 후 숫자와 결함
s = "".join(s)
print(s+sum)