# Dictionary
# 구분자 : ":", ","
# ":"는 key 값과 value 값을 구분하기 위한 구분자
# ","는 item 간의 구분
bar = {"김성관" : 12345, "하루나" : 67890, "김민정" : 98765, "하루나" : 5555}


print(bar["하루나"])  # 결과 : 5555

# json에서 value 값을 찾기 위해서는 무조건 key 값을 부여해줘야 함
# json은 dictionary 형태로 사용되는데, 여기에서 key 값은 value 값을 찾기 위한 인덱스 역할과
# 메타데이터로 사용할 수 있음