import socket
import os
import time

def udp_client(file_path, server_ip, server_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)  # Timeout de 1 segundo para espera de ACK

        file_size = os.path.getsize(file_path)
        sock.sendto(str(file_size).encode('utf-8'), (server_ip, server_port))

        with open(file_path, 'rb') as f:
            seq_num = 0
            while True:
                data = f.read(1024)
                if not data:
                    break
                packet = seq_num.to_bytes(4, byteorder='big') + data
                while True:
                    sock.sendto(packet, (server_ip, server_port))
                    try:
                        ack, _ = sock.recvfrom(1024)
                        if int.from_bytes(ack, byteorder='big') == seq_num:
                            break
                    except socket.timeout:
                        print(f"Timeout, retransmitting packet {seq_num}")
                seq_num += 1
                time.sleep(0.001)  # Ajuste o tempo de espera conforme necessário

        sock.sendto(b'EOF', (server_ip, server_port))
        print("File sent successfully.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()

# Exemplo de uso:
# udp_client('data/example_data.txt', '127.0.0.1', 65432)
