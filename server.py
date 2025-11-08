# Importa o módulo socket
from socket import *
import sys  # Necessário para encerrar o programa

# Define a porta do servidor
serverPort = 6789

# Cria o socket TCP (orientado à conexão)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor
# Associa o socket à porta escolhida e permite apenas uma conexão por vez
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print(f'Servidor rodando na porta {serverPort}...')

while True:
    # Estabelece a conexão
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print(f'Conexão estabelecida com: {addr}')

    try:
        # Recebe a mensagem do cliente (requisição HTTP)
        message = connectionSocket.recv(1024).decode()
        print(f'Requisição recebida:\n{message}')

        # Extrai o nome do arquivo solicitado
        filename = message.split()[1]
        f = open(filename[1:])  # remove o '/' inicial
        outputdata = f.read()

        # Envia a linha de status do cabeçalho HTTP
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        # Envia o conteúdo do arquivo ao cliente
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Fecha a conexão com o cliente
        connectionSocket.close()

    except IOError:
        # Envia mensagem de erro 404 se o arquivo não for encontrado
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>'.encode())

        # Fecha o socket do cliente
        connectionSocket.close()

# Fecha o socket principal (nunca é realmente alcançado, pois o servidor é contínuo)
serverSocket.close()
sys.exit()  # Encerra o programa
