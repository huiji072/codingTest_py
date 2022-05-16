food_times = [5, 0, 3, 3, 1]
k = 7

cnt = 0
answer = 0

while k+1>0:
    for j in range(len(food_times)):
        if food_times[j] == 0:
            continue
        else:
            k -= 1
            food_times[j] -= 1
            cnt += 1
            answer = j
            print(k, food_times)



print(answer+1)