# Importando sockets e definindo Host e porta do terminal. 
import socket
HOST = '127.0.0.1'     
PORT = 4000     
# Conectando servidor       
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
envi = (HOST, PORT)
tcp.connect(envi)
# Print na tela para informar o sucesso da conexão.
print ('Sistema conectado, aguardando requisição de senha')

# Criando condição para escolher tipo de senha (Normal ou preferencial) em padrão Utf-8.
while True:
    senha = input("\n Escolha seu tipo de senha: \n 1- Normal \n 2- Prioridade \n")
    if(senha== "1" or senha== "2"):
        if (senha == '1'):
            senha = "normal"
        else:
            senha = "prioridade"

        senha_encode = senha.encode('utf-8')
        tcp.send (senha_encode)
        print("Sucesso! Aguarde, sua senha será chamada em breve!")

# Aviso de erro ao gerar senha.
    else:
        print("\n Erro ao gerar senha! Por favor, tente novamente ou informe um de nossos atendentes.")
