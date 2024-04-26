# 거리를 'km' 단위로 입력받는다.
distance = int(input("여행할 거리를 킬로미터(km) 단위로 입력하세요: "))

# 빛의 속도를 기입한다.
speed = 299792

# '시간 = 거리/속도'
time = distance / speed

# 시간을 출력한다.
print("빛이", float(distance), "킬로미터를 여행하는 데 걸리는 시간은", time, end="초입니다.")