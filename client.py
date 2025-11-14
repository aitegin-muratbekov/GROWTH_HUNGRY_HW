# client.py
import socket

HOST = "127.0.0.1"   # тот же хост
PORT = 4000          # тот же порт

# СОЗДАЁМ TCP-КЛИЕНТСКИЙ СОКЕТ
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ПОДКЛЮЧАЕМСЯ К СЕРВЕРУ
client_socket.connect((HOST, PORT))

# ОТПРАВЛЯЕМ СООБЩЕНИЕ
message = "7+5"
client_socket.sendall(message.encode("utf-8"))

# ЖДЁМ ОТВЕТ
data = client_socket.recv(1024)
print("Reply from server:", data.decode("utf-8"))

# ЗАКРЫВАЕМ
client_socket.close()
