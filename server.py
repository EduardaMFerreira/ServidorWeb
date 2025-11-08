# Importa o módulo socket
from socket import *
import sys # Necessário para encerrar o programa

# Cria o socket TCP (orientado à conexão)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor

#Fill in start
#Fill in end

while True:

    # Estabelece a conexão
    print('Ready to serve...')
    connectionSocket, addr = #Fill in start #Fill in end
    
    try:
        # Recebe a mensagem do cliente (requisição HTTP)
        message = #Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start #Fill in end

        # Envia a linha de status do cabeçalho HTTP
        #Fill in start
        #Fill in end

        # Envia o conteúdo do arquivo ao cliente
        for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Fecha a conexão com o cliente
        connectionSocket.close()

    except IOError:
        # Envia mensagem de erro 404 se o arquivo não for encontrado
        #Fill in start
        #Fill in end

        # Fecha o socket do cliente
        #Fill in start
        #Fill in end

serverSocket.close()
sys.exit() # Encerra o programa