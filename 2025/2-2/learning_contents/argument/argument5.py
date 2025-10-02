# **는 딕셔너리
def prt(**arg):
    for key, value in arg.items():
        print(f"{key}, {value}")