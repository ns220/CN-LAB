import socket
import os

def handle_client(client_socket):
    file_name = client_socket.recv(1024).decode('utf-8')
    print(f"Request for file: {file_name}")

    if os.path.isfile(file_name):
        with open(file_name, 'rb') as file:
            file_data = file.read()
            client_socket.sendall(file_data)
    else:
        error_message = "Error: File not found."
        client_socket.sendall(error_message.encode('utf-8'))
    
    client_socket.close()

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  
    print(f"Server started on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()





import socket
def request_file(file_name, host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(file_name.encode('utf-8'))
    data = client_socket.recv(1024)
    if data:
        if data.decode('utf-8') == "Error: File not found.":
            print("File not found on server.")
        else:
            print("File contents received:")
            print(data.decode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    file_name = input("Enter the file name to request: ")
    request_file(file_name)
