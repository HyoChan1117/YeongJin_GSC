import json
# Serializer, Parser
# Data format, - JSON
# Python

bar = {"name" : "ycjung", "age" : 20, "roomnum" : [404, 511]}

# 네트워크로 전송 -> 문자열(text) -> Json
# bar는 메모리에 존재하는 데이터 -> Json Serializer
# -> Json 기반 Text


# dumps는 문자열로 저장 -> Python 객체를 json 문자열로 변환
# with open("test.txt", "w") as file_handler:
#     json.dump(bar, file_handler)

json_str = json.dumps(bar)

print(type(json_str))

# parsing
# loads는 json 문자열 -> Python 객체로 변환
rcvd_data = json.loads(json_str)

print(rcvd_data.get('phone'))
print(rcvd_data.get('name'))

print(type(rcvd_data['age']), type(rcvd_data['roomnum']), type(rcvd_data['name']))

# 1. get 방식
# 2. key 값을 이용해서 접근