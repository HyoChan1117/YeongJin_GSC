# client
import socket

HOST = "127.0.0.1"
PORT = 5500

# 1. socket 생성(IPv4 or IPv6, TCP or UDP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. connect (서버 주소, 서버 포트)
client_socket.connect((HOST, PORT))

# 사용자로부터 데이터 입력
send_msg = input("Input text: ")

# 입력된 데이터를 서버로 전송
# sendall 함수는 블락킹 함수 -> 전송이 끝나지 않으면 넘어가지 않음
client_socket.sendall(send_msg.encode('utf-8'))

# 서버로부터 수신한 데이터를 출력
rcvd_msg = client_socket.recv(1024).decode('utf-8')

print(f"[Client rcvd data]: {rcvd_msg}")