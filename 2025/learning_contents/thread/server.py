import socket
import threading

def handler_client(client_socket, client_addr):
    while True:
        rcvd_data = client_socket.recv(1024).decode('utf-8')
    
        if not rcvd_data:
            print("[Closed from client]")
            break
        
        print(f"[Rcvd data ({client_addr})]: {rcvd_data}")

        # 수신된 데이터를 전송
        client_socket.sendall(rcvd_data.encode('utf-8'))
        
    client_socket.close()

HOST = "127.0.0.1" # 서버의 IP 주소 -> 문자형
PORT = 12345 # 포트 주소 -> 정수형
num_of_threads = 0

# socket 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
server_socket.bind((HOST, PORT))

# listen
server_socket.listen(1)

print(f"[Listen] {HOST}, {PORT}")

while True:
    # accept -> 새로운 소켓을 생성
    client_socket, client_addr = server_socket.accept() 

    print(f"[Accept] {client_addr}")

    # 새로운 쓰레드 생성
    client_thread = threading.Thread(target=handler_client, args=(client_socket, client_addr))
    
    num_of_threads += 1
    print(f"쓰레드 생성 : {num_of_threads}")
    
    # 생성된 쓰레드 실행
    client_thread.start()


server_socket.close()