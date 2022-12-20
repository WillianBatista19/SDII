# Importando sockets e definindo Host e porta do terminal. 
import socket
HOST = '127.0.0.1'
PORT = 4000

# Conectando servidores com print para efeito estetico e de testes.
envi= (HOST, PORT)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(envi)
print("Conectando \n")

# Criando condição para chamar senha em padrão Utf-8 e mostrar na tela.

while True:

    if input("\n Aperte C para chamar a proxima senha: "):
        senha = str("c").encode('utf-8')
        print("Valor de SENHA: ", senha)
        tcp.send (senha)
        response = tcp.recv(1024).decode('utf-8')
    else: print("\n Erro ao chamar senha!")