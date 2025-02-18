# server
import socket

HOST = "127.0.0.1"
PORT = 5500

# 1. 소켓 생성 (TCP or UDP, IP 주소 버전: v4 or v6)
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP

# 2. bind (ip 주소, 포트 주소)
# 운영체제로부터 포트주소를 받아옴
# 127.0.0.1는 자기 자신을 가리키는 IP 주소
# 컴퓨터 내부에서만 사용 (외부 네트워크 접근 불가)
server_socket.bind((HOST, PORT))

# 3. listen(큐의 개수)
# 연결 요청을 위한 큐
# 클라이언트로부터 연결 요청을 받기 위한 listen
server_socket.listen(5)
print(f"[Listen] {HOST}, {PORT}")

# 4. accept() -> 사용자로부터 연결 요청을 받았을 때 - 새로운 소켓 생성
# 클라이언트 -> connect() : 클라이언트의 IP 주소와 포트주소를 받아옴
# accept는 클라이언트로부터 연결 요청이 왔을 때 멈춤이 풀려남
client_socket, client_addr = server_socket.accept()

print(f"[Accept] : {client_addr}")

# 무한루프
while True:
    # 5. recv(1024)
    # echo server
    # 클라이언트로부터 메시지를 수신
    # recv 함수는 동기 함수(블락킹 함수)여서 데이터가 없으면 넘어가지 않음음
    rcvd_data = client_socket.recv(1024).decode('utf-8')

    print(f"[Server: rcvd data]: {rcvd_data}")

    # 클라이언트가 소켓을 close할 때 -> 클라이언트가 close 함수를 사용하면 null값이 넘어옴
    # 클라이언트가 close 함수를 사용했을 때 참이 돼서 무한루프 탈출
    if not rcvd_data:
        break

    # 수신한 메시지를 클라이언트로 전송
    client_socket.sendall(rcvd_data.encode('utf-8'))

# 데이터 송수신이 끝나면 클라이언트 소켓과 서버 소켓을 닫아줘야 함
client_socket.close()
server_socket.close()

