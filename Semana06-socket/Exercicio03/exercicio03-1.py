#Importa Biblioteca socket
import socket
#Importa Biblioteca sys
import sys
#Define o endereço IP do dispositivo
TCP_IP = "127.0.0.1"
#Define a porta de comunicação e transferência de arquivos
FILE_PORT = 5005
#Define a porta de comunicação e transferência de dados
DATA_PORT = 5006
#Tamanho do buffer
buf = 1024
#Nome do arquivo
file_name = sys.argv[1]

try:
    #Especifica o tipo de endenreço IP aceito e indica o streaming de dados 
    sock = socket.socket(socket.
    AF_INET, socket.SOCK_STREAM)
    #Conexão do cliente ao endereço ADDR
    sock.connect((TCP_IP, FILE_PORT))
    #Envia o arquivo
    sock.send(file_name)
    #Encerra a transferência
    sock.close()
    #Mostra o status de envio
    print "Sending %s ..." % file_name
    #Abre o arquivo
    f = open(file_name, "rb")
    #Define o tipo de endereço IP utilizados
    sock = socket.socket(socket.
    AF_INET, socket.SOCK_STREAM)
    #Conecta cliente ao endereço ao ADDR do servidor
    sock.connect((TCP_IP, DATA_PORT))
    #Define a variável de leitura de dados
    data = f.read()
    #Envia os dados
    sock.send(data)

finally:
    #Encerra a transferência de arquivos
    sock.close()
    #Encerra a transferência de dados
    f.close()