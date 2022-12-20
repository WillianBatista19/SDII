import socket
import _thread

# Endereços IP do servidor e do TA, junto com suas respectivas Portas.

HOST = '127.0.0.1'    
PORT = 4000            
HOST_VISUALIZACAO = '127.0.0.2'
PORT_VISUALIZACAO = 5000

#Iniciando contagem de senhas

senha_normal = 1
contador = 0
senha_prioridade = 1

#Crinado arrays para armazenar senhas normais e com prioridade.

lista_normal = []
lista_prioridade = []

# Declarando variaveis e print dos termianis que conectarem ao servidor.

def conectado(con, cliente, udp, envi):
    print ('Terminal conectado: ', cliente)

# Criando condição o estilo de senha escolhida, colocando em padrão Utf-8 e enviando para o TA, para esperar chamada de senha.

    while True:

        global lista_normal,lista_prioridade
        global senha_normal, senha_prioridade, contador

        senha = con.recv(1024).decode('utf-8')
        print("SENHA NO SERVIDOR:", senha)

        if (senha == "normal"):
            senha = senha+str(senha_normal)
            lista_normal.append(senha)
            senha_normal+=1

        elif (senha == "prioridade"): 
            senha = senha+str(senha_prioridade)
            lista_prioridade.append(senha)
            senha_prioridade+=1

        elif (senha == 'c'):
            if(len(lista_normal) > 0 and contador < 2):
                if len(lista_normal) >0:
                    senha_tcp = "Senha "+str(lista_normal[0])
                    senha_udp = "Senha "+str(lista_normal[0])
                    res_udp = (senha_udp).encode('utf-8')
                    res_tcp = (senha_tcp).encode('utf-8')
                    con.send(res_tcp) 
                    udp.sendto (res_udp,envi)
                    lista_normal.pop(0)
                    if (len(lista_normal) > 0 and len(lista_prioridade) > 0):
                        contador+=1
                    elif (len(lista_prioridade) == 0):
                        contador=0
                    else:
                        contador=2

                 # Aviso em caso de falta de senha Normal.

                else:
                    res = ("\n Sem senha normal").encode('utf-8')
                    con.send(res)

            elif(len(lista_prioridade) > 0 and contador == 2 or len(lista_prioridade) > 0 and len(lista_normal) == 0 and contador == 0):
                if len(lista_prioridade) > 0:
                    senha_tcp = "Senha "+str(lista_prioridade[0])
                    senha_udp = "Senha "+str(lista_prioridade[0])
                    res_udp = (senha_udp).encode('utf-8')
                    res_tcp = (senha_tcp).encode('utf-8')
                    con.send(res_tcp)
                    udp.sendto (res_udp, envi)
                    lista_prioridade.pop(0)
                    if (len(lista_prioridade) > 0 and len(lista_normal) > 0):
                        contador=0
                    elif ((len(lista_prioridade) > 0 and len(lista_normal) == 0)):
                        contador=2
                    elif ((len(lista_prioridade) == 0 and len(lista_normal) > 0)):
                        contador=0

                # Aviso em caso de falta de senha prioritaria.

                else:
                    res = ("\n Sem senha prioritária").encode('utf-8')
                    con.send(res)

        # Erro e encerramento estrutura em falta de Senhas disponiveis.

        if not senha:
            print("\n Sem senha disponivel")
            break

    # Informando o fim da conexão

    print ('\n conexão encerrada')
    con.close

# Configurações basicas de sockts para conexões. Protocolos TCP e UDP sendo configurados. 

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen()

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
envi = (HOST_VISUALIZACAO, PORT_VISUALIZACAO)

# Configurando condição para uso de thread, permitindo multiplas conexões.

while True:
    con, cliente = tcp.accept()
    _thread.start_new_thread(conectado,(con, cliente, udp, envi))
