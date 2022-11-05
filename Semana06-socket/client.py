#Importa Biblioteca socket
import socket
#Define o número de bytes enviados pelo servidor do cliente
HEADER = 64
#Define a porta de comunicação
PORT = 5050
#Define o formato de codificação binária UFT-8
FORMAT = 'utf-8'
#Criação da mensagem de desconexão
DISCONNECT_MESSAGE = "!DISCONNECT"
#Atribui o endereço IP para SERVER
SERVER = "192.168.1.26"
#Associa o servidor à porta de comunicação por meio da variável ADDR
ADDR = (SERVER, PORT)
#Especifica qual o tipo de endereço IP aceito para conexão e indica o streaming de dados
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Conecta o cliente usando o ADDR
client.connect(ADDR)

#Função que envia as mensagens ao servidor
def send(msg):
    #Passa a string para byte
    message = msg.encode(FORMAT)
    #Pega o tamanho da mensagem
    msg_length = len(message)
    #Passa o tamnha da mensagem para sua transformação em byte
    send_length = str(msg_length).encode(FORMAT)
    #Passa para a mensagem 64bytes
    send_length += b' ' * (HEADER - len(send_length))
    #Envia o tamanho da mensagem para o servidor
    client.send(send_length)
    #Envia a mensagem para o servidor
    client.send(message)
    #Decodifica a mensagem
    print(client.recv(2048).decode(FORMAT))

#Envia mensagens 
send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")
#Desconecta
send(DISCONNECT_MESSAGE)