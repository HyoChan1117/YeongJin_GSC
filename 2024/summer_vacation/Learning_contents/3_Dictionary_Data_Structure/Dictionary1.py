bar = { "name" : "ycjung", "age" : 20, "phone" : 123-456 }

bar['email'] = "ycjung@yju.ac.kr"


# age가 있으면 Skip하고 없으면 추가해라.

if "email" in bar:
    print("True")
else:
    print("False")

if "mobile" in bar.keys():
    print("True")
else:
    print("False")