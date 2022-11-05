#Importa Biblioteca socket
import socket
#Importa Biblioteca select
import select

#Define o endereço UDP_IP do dispositivo
UDP_IP = "127.0.0.1"
#Define a porta de comunicação e transferência de arquivos
IN_PORT = 5005
#Define o timeout
timeout = 3

#Especifica o tipo de endenreço IP aceito e indica o streaming de dados
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Vincula o socket ao endereço ADDR
sock.bind((UDP_IP, IN_PORT))

while True:
    #Define o tamanho do arquivo recebido
    data, addr = sock.recvfrom(1024)
    if data:
        #Mostra o nome do arquivo
        print "File name:", data
        file_name = data.strip()

    #Abre o arquivo para escrita
    f = open(file_name, 'wb')

    
    while True:
        #Recebe e lê as transferências
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            #define o tamanho do arquivo recebido
            data, addr = sock.recvfrom(1024)
            #escreve os dados no arquivo
            f.write(data)
        else:
            #Mostra o status de transferência
            print "%s Finish!" % file_name
            #Encerra a conexão
            f.close()
            break