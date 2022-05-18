n = int(input())

arr = list(map(int, str(n)))

arr_len = len(arr) // 2

a = sum(arr[:arr_len])
b = sum(arr[arr_len:])

if a == b:
    print("LUCKY")
else:
    print("READY")