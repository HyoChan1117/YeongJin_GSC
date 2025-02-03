# server
import socket

# 1. 소켓 생성 (TCP or UDP, IP 주소 버전: v4 or v6)
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP

# 2. bind (ip 주소, 포트 주소)
# 127.0.0.1는 자기 자신을 가리키는 IP 주소
# 컴퓨터 내부에서만 사용 (외부 네트워크 접근 불가)
server_socket.bind(("127.0.0.1", 5500))

# 3. listen(큐의 개수)
server_socket.listen(5)
print(f"listen on 127.0.0.1 : 5500")


# 4. accept() -> 사용자로부터 연결 요청을 받았을 때 - 새로운 소켓 생성
# 클라이언트 -> connect()
server_socket.accept()

print("Hello")