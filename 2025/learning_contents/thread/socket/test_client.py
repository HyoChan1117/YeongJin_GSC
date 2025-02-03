# client
import socket

# 1. socket 생성(IPv4 or IPv6, TCP or UDP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. connect (서버 주소, 서버 포트)
client_socket.connect(("127.0.0.1", 5500))