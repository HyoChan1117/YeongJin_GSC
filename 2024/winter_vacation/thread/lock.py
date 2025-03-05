import threading

my_lock = threading.Lock()

# Target Function
def bar():
    for count in range(1, 6):
        with my_lock:  # 락 획득
            print(f"bar: {count}")

def foo():
    for count in range(1, 6):
        with my_lock:  # 락 획득
            print(f"foo: {count}")

thread1 = threading.Thread(target=bar)
thread2 = threading.Thread(target=foo)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("finish")
