import socket

HOST = "127.0.0.1"
PORT = 12345

# 소켓 생성
# IPv4 or IPv6 선택 / TCP or UDP 선택택
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding
# bind 함수 괄호 안에는 튜플 형태가 들어감감
server_socket.bind((HOST, PORT))

# listen
server_socket.listen(1)

# accept -> 새로운 소켓 생성
client_socket, client_address = server_socket.accept()

# 종료
server_socket.close()
client_socket.close()

