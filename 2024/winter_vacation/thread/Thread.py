import threading
from time import sleep

balance = 0

def deposit():
    amount = 10
    for count in range(10):
        balance = balance + amount
        sleep(0.01)
        print("Deposit!, balance : [balance]")

def withdraw():
    pass

thread_1 = threading.Thread(target=deposit)
thread_2 = threading.Thread(target=withdraw)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f"[balance]: {balance}")