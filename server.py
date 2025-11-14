# server.py
import socket

HOST = "127.0.0.1"   # локальный компьютер
PORT = 4000          #

# СОЗДАЁМ TCP-СЕРВЕРНЫЙ СОКЕТ
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server is running on {HOST}:{PORT} ...")

while True:
    conn, addr = server_socket.accept()
    print(f"Client connected from {addr}")

    data = conn.recv(1024)
    if not data:
        conn.close()
        continue

    message = data.decode("utf-8")

    print(f"Received from client: {message}")

    reply = f"Server received: {int(message[0])+ int(message[2])}"
    conn.sendall(reply.encode("utf-8"))

    conn.close()
    print("Connection closed\n")
