#Importando socket
import socket

# Definindo Host e porta do terminal.
HOST = '127.0.0.2'
PORT = 5000

#Conectando os terminais.

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

# Adicionando Print para efeito estetico e de testes.

print("Sucesso ao iniciar TV, no aguardo de senhas!\n")

# Criando condição para transformar senha em padrão Utf-8 e mostrar na tela, quando disponivel.

while True:
    senha, cliente = udp.recvfrom(1024)
    senha = senha.decode('utf-8')

    print (senha)

