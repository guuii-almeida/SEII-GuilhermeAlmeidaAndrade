#Importa Biblioteca socket
import socket
#Importa Biblioteca time
import time
#Importa Biblioteca sys
import sys

#Define o endereço UDP_IP do dispositivo
UDP_IP = "127.0.0.1"
#Define a porta de comunicação e transferência de arquivos
UDP_PORT = 5005
#Tamanho do buffer
buf = 1024

file_name = sys.argv[1]


#Especifica o tipo de endenreço IP aceito e indica o streaming de dados
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Conecta a ADDR por meio da sendto
sock.sendto(file_name, (UDP_IP, UDP_PORT))
#Mostra a tela de status de transferência
print "Sending %s ..." % file_name

#Abre o arquivo para leitura
f = open(file_name, "r")
#Define o tamanho dos arquivos
data = f.read(buf)

while(data):
    #Verifica a variável de leitura e do tamamho do arquivo
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        #define o a tamanho dos dados
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save

#Encerra a transmissão
sock.close()
#Encerra a transferência dos dados
f.close()