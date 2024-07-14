dict_num = {}

dict_num["key"] = "value"
dict_num["key1"] = "value1"

print(list(dict_num.keys()))

for key, value in dict_num.items():
    print(key, value)