import sys
from tcp_client import tcp_client
from tcp_server import tcp_server
from udp_client1 import udp_client
from udp_server import udp_server

def main():
    if len(sys.argv) < 5:
        print("Uso: python main.py <tipo> <modo> <arquivo> <ip> <porta>")
        print("  <tipo>  : 'tcp' ou 'udp'")
        print("  <modo>  : 'client' ou 'server'")
        print("  <arquivo> : caminho do arquivo a ser enviado (apenas no modo client)")
        print("  <ip>    : endereço IP do servidor")
        print("  <porta> : número da porta do servidor")
        return

    tipo = sys.argv[1]
    modo = sys.argv[2]
    file_path = sys.argv[3]
    server_ip = sys.argv[4]
    server_port = int(sys.argv[5])

    if tipo == 'tcp':
        if modo == 'client':
            tcp_client(file_path, server_ip, server_port)
        elif modo == 'server':
            tcp_server(server_ip, server_port)
        else:
            print("Modo inválido. Escolha 'client' ou 'server'.")
    elif tipo == 'udp':
        if modo == 'client':
            udp_client(file_path, server_ip, server_port)
        elif modo == 'server':
            udp_server(server_ip, server_port)
        else:
            print("Modo inválido. Escolha 'client' ou 'server'.")
    else:
        print("Tipo inválido. Escolha 'tcp' ou 'udp'.")

if __name__ == "__main__":
    main()


'''
# refused
python src\main.py tcp client data\example_data.txt 127.0.0.1 65432

# ok
python src\main.py tcp client data\example_data.txt 127.0.0.1 62699
'''