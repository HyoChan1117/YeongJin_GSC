now_time = list(map(int, input().split(" ")))
oven_time = int(input())

if now_time[1] + oven_time <= 60:
    now_time[1] += oven_time
else:
    if (now_time[1] + oven_time) % 60 == 0:
        now_time[0] += ((now_time[1] + oven_time) // 60)
        now_time[1] = 0
    else:
        now_time[1] += oven_time - 60
        now_time[0] += 1

if now_time[0] >= 24:
    now_time[0] = 0

print(now_time[0], now_time[1])