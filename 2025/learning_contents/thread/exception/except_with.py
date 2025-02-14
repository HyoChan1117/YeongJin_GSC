import socket
try:
    print("시작")
    
    # with를 사용하면 with문이 종료되는 순간 자원이 자동으로 반납됨
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
    
        my_socket.connect(("127.0.0.1", 12345)) # 서버가 동작하지 않을 때, 나의 네트워크에 문제가 생겼을 때
        
        print(my_socket.recv(1024).decode('utf-8'))  # 연결이 비상적으로 종료 되었을 때
    
except:
    print("소켓 예외 발생")
# 예외가 처리되던 안되던 무조건 실행해야 하는 코드는 finally에 작성
finally:
    my_socket.close()
    
print("종료")