# TCP의 client 소켓

# 반드시 필요한 단계
# 1. TCP 소켓 생성 -> TCP 방식, client
# -> AF_INET(IPv4), SOCK_STREAM(TCP) 사용
# 2. 서버 주소와 포트에 연결 요청
# -> 특정 프로그램에 접근하기 위해서는 IP주소와 포트 주소가 필요
# 3. 데이터를 보냄(send) - 서버로 데이터 전송
# 4. 데이터를 받음(receive) - 서버로부터 데이터 수신
# 5. 소켓(socket) 종료

import socket

def run_client():
    """클라이언트 실행 함수"""
    host = '127.0.0.1'  # 서버 호스트 주소 (localhost)
    port = 12345        # 서버 포트 번호

    # TCP 소켓 생성 (IPv4, TCP 방식)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 지정된 서버 주소와 포트에 연결 요청
    client_socket.connect((host, port))
    print("서버에 연결되었습니다. 메시지를 입력하세요 (종료하려면 'exit' 입력).")

    try:
        while True:
            # 사용자 입력을 받음
            message = input(">>> ")
            # lower()는 소문자
            if message.lower() == 'exit':  # 'exit' 입력 시 연결 종료
                print("서버와의 연결을 종료합니다.")
                break
            
            # 입력한 메시지를 서버로 전송 (UTF-8 인코딩)
            # 입력 받은 String 문자열을 utf-8로 인코딩해서 보냄
            client_socket.sendall(message.encode('utf-8'))
    except Exception as e:
        print(f"오류 발생: {e}")  # 예외 발생 시 오류 메시지 출력
    finally:
        client_socket.close()  # 클라이언트 소켓 닫기
        print("클라이언트가 종료되었습니다.")

if __name__ == "__main__":
    run_client()  # 클라이언트 실행
