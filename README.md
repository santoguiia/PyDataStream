# PyFileTransfer

## Descrição

PyFileTransfer é um projeto implementado em Python que demonstra a transmissão de arquivos usando sockets TCP e UDP. Este repositório contém dois programas distintos:

1. **Transmissão TCP:**
   - O cliente lê um arquivo e o transmite em pedaços (pacotes) até um servidor.
   - O servidor recebe os pacotes e grava o arquivo usando um nome qualquer.

2. **Transmissão UDP:**
   - O cliente lê um arquivo e o transmite em pacotes UDP até um servidor.
   - O servidor recebe os pacotes e grava o arquivo.

## Funcionalidades

- **Transmissão TCP:**
  - Confiabilidade garantida pela natureza do protocolo TCP.
  - Fragmentação e reconstituição de arquivos.
  - Manejo de conexões cliente-servidor.

- **Transmissão UDP:**
  - Transmissão rápida de arquivos com menor sobrecarga de rede.
  - Gerenciamento de pacotes UDP, que não garantem entrega ou ordem.
  - Implementação de lógica adicional para reordenação e verificação de integridade.

## Requisitos

- Python 3.x
- Bibliotecas padrão de sockets

## Como Usar

### Transmissão TCP

1. **Servidor:**
   ```sh
   python tcp_server.py
   ```

2. **Cliente:**
   ```sh
   python tcp_client.py caminho/para/seu/arquivo
   ```

### Transmissão UDP

1. **Servidor:**
   ```sh
   python udp_server.py
   ```

2. **Cliente:**
   ```sh
   python udp_client.py caminho/para/seu/arquivo
   ```

## Estrutura do Projeto

- `tcp_server.py` - Código do servidor TCP.
- `tcp_client.py` - Código do cliente TCP.
- `udp_server.py` - Código do servidor UDP.
- `udp_client.py` - Código do cliente UDP.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.
