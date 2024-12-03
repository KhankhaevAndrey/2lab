import socket

def run_udp_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message = input("Введите сообщение: ")
        client_socket.sendto(message.encode('utf-8'), (host, port))

        data, addr = client_socket.recvfrom(1024)
        print(f"Получен ответ от сервера: {data.decode('utf-8')}")

if __name__ == "__main__":
    run_udp_client()

