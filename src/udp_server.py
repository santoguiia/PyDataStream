import socket
import time

def udp_server(server_ip, server_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((server_ip, server_port))
        print(f"UDP server listening on {server_ip}:{server_port}")

        file_size, addr = sock.recvfrom(1024)
        file_size = int(file_size.decode('utf-8'))
        received_size = 0
        expected_seq_num = 0
        start_time = time.time()

        with open('received_file_udp.txt', 'wb') as f:
            while received_size < file_size:
                data, addr = sock.recvfrom(1024 + 4)
                if data == b'EOF':
                    break
                seq_num = int.from_bytes(data[:4], byteorder='big')
                if seq_num == expected_seq_num:
                    f.write(data[4:])
                    received_size += len(data) - 4
                    expected_seq_num += 1
                ack = seq_num.to_bytes(4, byteorder='big')
                sock.sendto(ack, addr)

        end_time = time.time()
        print(f"File received in {end_time - start_time:.2f} seconds.")
    except KeyboardInterrupt:
        print("Server stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()

# Exemplo de uso:
# udp_server('127.0.0.1', 65432)
