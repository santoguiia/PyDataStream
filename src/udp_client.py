import socket
import os
import time

def udp_client(file_path, server_ip, server_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        file_size = os.path.getsize(file_path)
        sock.sendto(str(file_size).encode('utf-8'), (server_ip, server_port))

        with open(file_path, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                sock.sendto(data, (server_ip, server_port))
                time.sleep(0.001)  # Ajuste o tempo de espera conforme necessário

        sock.sendto(b'EOF', (server_ip, server_port))
        print("File sent successfully.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()
