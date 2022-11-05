#Importa Biblioteca socket
import socket

#Define o endereço IP do dispositivo
TCP_IP = "127.0.0.1"
#Define a porta de comunicação e transferência de arquivos
FILE_PORT = 5005
#Define a porta de comunicação e transferência de dados
DATA_PORT = 5006
#Define o timeout
timeout = 3
#Tamanho do buffer
buf = 1024

#Especifica o tipo de endereço IP aceito e indica o streaming de dados
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Vincula o socket ao endereço ADDR
sock_f.bind((TCP_IP, FILE_PORT))
#Escuta possíveis conexões
sock_f.listen(1)
#Especifica o tipo de endereço IP utilizado
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Vincula o socket ao endereço ADDR
sock_d.bind((TCP_IP, DATA_PORT))
#Escuta possíveis conexões
sock_d.listen(1)


while True:
    #Conexões admitidas pelo servidor
    conn, addr = sock_f.accept()
    #Define o tamanho da mensagem
    data = conn.recv(buf)
    if data:
        #Mostra o nome do arquivo
        print "File name:", data
        #Tira os bytes iniciais e finais do arquivo
        file_name = data.strip()

    #Abertura do arquivo para escrita
    f = open(file_name, 'wb')
    #Conexões do arquivo para escrita
    conn, addr = sock_d.accept()
    while True:
        #Define o tamanho dos dados
        data = conn.recv(buf)
        if not data:
            break
        #Escreve os dados no arquivo
        f.write(data)
    #Mostra o status de transferência finalizada
    print "%s Finish!" % file_name
    #Encerra a conexão
    
    f.close()