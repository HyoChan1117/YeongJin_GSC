import threading

# Target Function
def bar():
    for _ in range(5):
        print("Hello")

# 생성상태(New)
my_thread = threading.Thread(target=bar)
my_thread.daemon = False  # 논데몬 쓰레드

# 준비상태(Runnable)
my_thread.start()

# 모든 쓰레드드가 종료될 때까지 대기 -> 프로그램의 실행 흐름을 기다림
my_thread.join()

# 준비상태와 실행상태는 반복(loap)됨

print("Finish")
