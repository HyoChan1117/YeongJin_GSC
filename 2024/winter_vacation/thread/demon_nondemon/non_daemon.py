import threading

# Target Function
def bar():
    for _ in range(5):
        print("Hello")

# 생성상태(New)
my_thread = threading.Thread(target=bar, daemon=False)

# 준비상태(Runnable)
my_thread.start()

# 준비상태와 실행상태는 반복(loap)됨

print("Finish")
