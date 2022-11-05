#Importa Biblioteca socket
import socket 
#Importa Biblioteca threading
import threading

#Define o número de bytes recebidos pelo servidor do cliente
HEADER = 64
#Define a porta de comunicação
PORT = 5050
#Atribui o endereço IP local para SERVER
SERVER = socket.gethostbyname(socket.gethostname())
#Associa o servidor à porta de comunicação por meio da variável ADDR
ADDR = (SERVER, PORT)
#Define o formato de codificação binária UFT-8
FORMAT = 'utf-8'
#Criação da mensagem de desconexão
DISCONNECT_MESSAGE = "!DISCONNECT"
#Especifica qual o tipo de endereço IP aceito para conexão e indica o streaming de dados
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Vincula o socket ao endereço ADDR
server.bind(ADDR)

#Função que faz a administração das configurações de conexão entre o servidor e cliente
def handle_client(conn, addr):
    #Mensagem de conexão
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        #Define o número de bytes da mensagem
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            #Converte para uma variável inteira o número de bytes
            msg_length = int(msg_length)
            #Atribui a mensagem à uma variável
            msg = conn.recv(msg_length).decode(FORMAT)
            #Verifica a mensagem recebida
            if msg == DISCONNECT_MESSAGE:
                connected = False
            #Imprime o endereço do cliente e a mensagem
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
    #Finaliza a conexão
    conn.close()
        
#Função que permite a administração das conexões pelo servidor
def start():
    #Escuta conexões
    server.listen()
    #Mostra o status do servidor
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        #Conexões admitidas pelo servidor
        conn, addr = server.accept()
        #Thead que envia conexões para o handle_client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        #Inicia a thread
        thread.start()
        #Mostra as conexões ativas
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

#Indica a inicialização do servidor
print("[STARTING] server is starting...")
start()