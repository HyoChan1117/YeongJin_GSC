
msg = "hello"

def setMsg(argMsg) :        # def
    msg = argMsg + "hello"  # msg 변수는 언제 태어나는지
    print(msg)
    
setMsg("안녕하세요")


print(msg)