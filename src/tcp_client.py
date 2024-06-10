import socket
import os

def tcp_client(file_path, server_ip, server_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_ip, server_port))

        file_size = os.path.getsize(file_path)
        sock.sendall(str(file_size).encode('utf-8'))

        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                sock.sendall(data)

        print("File sent successfully.")
    except ConnectionRefusedError:
        print(f"Connection refused by server at {server_ip}:{server_port}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()
