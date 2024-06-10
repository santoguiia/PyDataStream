import socket
import time

def tcp_server(server_ip, server_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((server_ip, server_port))
        sock.listen(1)
        print(f"TCP server listening on {server_ip}:{server_port}")

        while True:
            conn, addr = sock.accept()
            print(f"Accepted connection from {addr}")

            file_size = int(conn.recv(1024).decode('utf-8'))
            received_size = 0
            start_time = time.time()

            with open('received_file_tcp.txt', 'wb') as f:
                while received_size < file_size:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
                    received_size += len(data)

            end_time = time.time()
            print(f"File received in {end_time - start_time:.2f} seconds.")
            conn.close()
    except KeyboardInterrupt:
        print("Server stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()
