data = input()
r = int(data[1])
c = int(ord(data[0])) - int(ord('a')) + 1
array = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

cnt = 0
for arr in array:
    nr = r + arr[0]
    nc = c + arr[1]
    if nr < 1 or nc < 1 or nr > 8 or nc > 8:
        continue
    cnt += 1
print(cnt)
