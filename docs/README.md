## Entendendo o Funcionamento dos Servidores TCP e UDP

### O que são servidores?

Servidores são programas que ficam em execução contínua, aguardando conexões ou solicitações de outros programas, chamados de clientes. Eles fornecem serviços específicos, como enviar arquivos, hospedar sites, gerenciar bancos de dados, etc.

### Servidores TCP (Transmission Control Protocol)

* **Conexão confiável:** Estabelecem uma conexão formal entre o cliente e o servidor antes de iniciar a transferência de dados.
* **Garantia de entrega:** Garantem que todos os dados enviados cheguem ao destino na ordem correta e sem erros.
* **Comunicação bidirecional:** Permitem que o cliente e o servidor enviem e recebam dados simultaneamente.
* **Exemplo:** Transferência de arquivos grandes, navegação na web, e-mail.

### Servidores UDP (User Datagram Protocol)

* **Conexão sem estado:** Não estabelecem uma conexão formal antes de enviar dados.
* **Sem garantia de entrega:** Não garantem que os dados cheguem ao destino, nem que cheguem na ordem correta.
* **Comunicação unidirecional:** Os dados são enviados em pacotes individuais, sem confirmação de recebimento.
* **Exemplo:** Streaming de vídeo, jogos online, chamadas de voz e vídeo.

### Por que os servidores ficam em execução contínua?

Servidores precisam ficar em execução contínua para estarem disponíveis para atender a solicitações de clientes a qualquer momento. Se um servidor fosse encerrado após cada conexão, ele não estaria disponível para atender a outras solicitações.

### Como os servidores TCP e UDP funcionam no seu projeto?

No seu projeto `PyDataStream`, os scripts `tcp_server.py` e `udp_server.py` implementam servidores TCP e UDP simples para transferência de arquivos.

* **`tcp_server.py`:**
    1. O servidor TCP escuta em uma porta específica.
    2. Quando um cliente se conecta, ele recebe o tamanho do arquivo a ser enviado.
    3. O servidor recebe os dados do arquivo em blocos de 1024 bytes até que todo o arquivo seja recebido.
    4. O servidor salva o arquivo recebido em um arquivo local.

* **`udp_server.py`:**
    1. O servidor UDP escuta em uma porta específica.
    2. Ele recebe o tamanho do arquivo a ser enviado.
    3. O servidor recebe os dados do arquivo em pacotes UDP de 1024 bytes.
    4. Quando recebe um pacote especial "EOF" (End of File), o servidor sabe que a transferência terminou.
    5. O servidor salva o arquivo recebido em um arquivo local.

**Observação:**

A escolha entre TCP e UDP depende dos requisitos da sua aplicação. Se você precisa de uma transferência de arquivos confiável e ordenada, use TCP. Se a velocidade e a eficiência são mais importantes do que a confiabilidade, use UDP.
