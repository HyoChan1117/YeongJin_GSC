# TCP의 client 소켓

# 반드시 필요한 단계
# 1. TCP 소켓 생성 -> TCP 방식, client
# -> AF_INET(IPv4), SOCK_STREAM(TCP) 사용
# 2. 바인딩(binding)
# -> 클라이언트로부터 요청을 받고, 그 요청을 처리해 주기 위해서는 IP주소와 포트주소가
#    필요함. IP주소와 포트주소를 운영체제로부터 받아와야 하기 때문에 바인딩이 필요함
# 3. listen
# -> 서버가 클라이언트의 요청을 기다려야 함 : 클라이언트의 연결 요청을 수락해야 함

# 위의 1, 2, 3번은 클라이언트로부터 연결 요청을 받기 위한 소켓을 생성

# 4. 데이터를 받음(receive) - 서버로부터 데이터 수신
# 5. 소켓(socket) 종료

import socket

def run_server():
    """싱글 스레드 TCP 서버 실행 함수"""
    host = '127.0.0.1'  # 서버 호스트 주소 (localhost)
    port = 12345        # 사용할 포트 번호

    # TCP 소켓 생성 (IPv4, TCP 방식)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 서버 소켓에 IP와 포트 바인딩
    server_socket.bind((host, port))
    
    # 클라이언트의 접속을 기다림 (최대 5개 대기 가능) -> Queue의 개수가 5개
    # listen을 하면 IP주소와 포트주소가 이미 넘어옴옴
    server_socket.listen(5)
    
    print(f"서버가 {host}:{port}에서 대기 중입니다...")
    
    try:
        while True:
            # 클라이언트의 연결 요청 수락 (하나씩 처리)
            # 클라이언트로부터 연결 요청이 왔을 때, accept가 활성화
            # 소켓을 새롭게 하나 더 생성
            client_socket, client_address = server_socket.accept()  # accept를 실행하면 프로그램의 실행이 멈춤춤
            print(f"클라이언트 연결됨: {client_address}")
            
            try:
                while True:
                    # 클라이언트로부터 메시지 수신 (최대 1024바이트)
                    message = client_socket.recv(1024).decode('utf-8')
                    if not message:  # 메시지가 없으면 연결 종료
                        print(f"클라이언트 연결 종료: {client_address}")
                        break
                    print(f"[{client_address}] {message}")  # 받은 메시지 출력
                    
                    # 에코(받은 메시지를 다시 클라이언트에게 전송)
                    client_socket.sendall(f"서버 응답: {message}".encode('utf-8'))
            except Exception as e:
                print(f"클라이언트 처리 중 오류 발생: {e}")
            finally:
                client_socket.close()  # 클라이언트 소켓 종료
    except KeyboardInterrupt:
        print("서버가 종료되었습니다.")
    finally:
        server_socket.close()  # 서버 소켓 닫기

if __name__ == "__main__":
    run_server()  # 서버 실행
