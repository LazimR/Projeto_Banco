

import datetime
from random import randint
import mysql.connector
import socket
import threading
from datetime import datetime

class usuario(threading.Thread):
    def __init__(self,adress,con) -> None:
        threading.Thread.__init__()
        self.con = con
        self.adress = adress
        print('Nova conexao:',con)

    def run(self):
        while(True):
#       0 - Cadastro | 1 - Login | 2 - Deposito | 3 - Saque | 4 - Transferência | 5 - Extrato
            try:
                operacao = con.recv(1024).decode()
                operacao = operacao.split(',')

    #           -------- CADASTRO --------
                if operacao[0] == '0':
                    print('Cadastro\n')
                    print(operacao)
                    #restante dos valores | 1 == nome | 2 == cpf | 3 == login | 4 == senha
                    query = 'SELECT cpf, login FROM conta WHERE cpf = %s OR login = %s'
                    values = (operacao[2],operacao[3])
                    cursor.execute(query,values)
                    consulta = cursor.fetchall()
                    print(consulta)
                    
                    if len(consulta) == 0:
                        query = 'SELECT numero FROM conta'
                        cursor.execute(query)
                        aux = cursor.fetchall()
                        n = gera_numero(aux)

                        query = 'INSERT INTO conta (nome, cpf, numero, saldo, login, senha) VALUES (%s, %s, %s, %s, %s, MD5(%s))'
                        
                        values = (operacao[1],operacao[2],n,'0',operacao[3],operacao[4])
                        cursor.execute(query,values)
                        # 1 == Sucesso na operação
                        con.send(f'1,{n}'.encode())
                    else:
                        # 0 == Login/CPF já em uso
                        con.send('0'.encode())

    #           -------- LOGIN --------
                elif operacao[0] == '1':
                    print('Login')
                    #restante dos valores | 1 == login | 2 == senha
                    query = 'SELECT login,senha,nome,numero FROM conta'
                    cursor.execute(query)
                    consulta = cursor.fetchall()
                    dados = []
                    for i in consulta:
                        if i[0] == operacao[1]:
                            dados = i
                    
                    if dados[1] == operacao[2]:
                        # 1 == Sucesso na operação
                        con.send(f'1,{dados[2]},{dados[3]}'.encode())
                    else:
                        # 0 == Senha/Login incorreto
                        con.send('0'.encode())

    #           -------- DEPOSITO --------
                elif operacao[0] == '2':
                    print('Deposito')
                    #restante dos valores | 1 == numero | 2 == quantidade
                    if float(operacao[2]) > 0:
                        print('entrou')
                        query = 'UPDATE conta SET saldo = saldo + %s WHERE numero = %s'
                        values = (operacao[2],operacao[1])
                        cursor.execute(query,values)
                        data = datetime.now()
                        data = data.strftime('%Y-%m-%d %H:%M:%S')
                        query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                        values = (f'Deposito:{operacao[2]} - Data:{data}',data,operacao[1])
                        cursor.execute(query,values)
                        query = 'SELECT saldo,numero FROM conta'
                        cursor.execute(query)
                        consulta = cursor.fetchall()
                        saldo = []
                        for i in consulta:
                            if i[1] == operacao[1]:
                                saldo = i[0]

                        # 1 == Sucesso na operação
                        con.send(f'1,{saldo}'.encode())
                    else:
                        # 0 == Quantidade negativa/nula
                        con.send('0'.encode())

    #           -------- SAQUE --------
                elif operacao[0] == '3':
                    print('Saque')
                    #restante dos valores | 1 == senha | 2 == numero | 3 == valor
                    query = 'SELECT senha,numero,saldo FROM conta'
                    cursor.execute(query)
                    print('Passou do primeiro execute')
                    consulta = cursor.fetchall()
                    
                    dados = []
                    for i in consulta:
                        if str(i[1]) == str(operacao[2]):
                            dados = i

                    if str(operacao[1]) == str(dados[0]):
                        print('Senha correta')
                        if float(dados[2]) >= float(operacao[3]):
                            print('saldo suficiente')
                            query = 'UPDATE conta SET saldo = saldo - %s WHERE numero = %s'
                            values = (operacao[3],operacao[2])
                            cursor.execute(query,values)
                            print('Passou pelo segundo execute')
                            data = datetime.now()
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                            query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                            cursor.execute(query,(f'Saque:{operacao[3]} - Data:{data}',data,operacao[2]))
                            query = 'SELECT saldo,numero FROM conta'
                            cursor.execute(query)
                            consulta = cursor.fetchall()
                            saldo = []
                            for i in consulta:
                                if i[1] == operacao[1]:
                                    saldo = i[0]
                            # 1 == Sucesso na operação
                            con.send(f'1,{saldo}'.encode())
                        else:
                            # 2 == Saldo insuficiente
                            con.send('2'.encode())
                    else:
                        # 0 == Senha incorreta
                        con.send('0'.encode())

    #           -------- TRANSFERÊNCIA --------      
                elif operacao[0] == '4':
                    #restante dos valores | 1 == senha | 2 == numero R. | 3 == numero D. | 4 == valor
                    
                    query = 'SELECT senha,numero,saldo FROM conta'
                    cursor.execute(query)
                    print('Passou do primeiro execute')
                    consulta = cursor.fetchall()
                    
                    dados = []
                    for i in consulta:
                        if str(i[1]) == str(operacao[2]):
                            dados = i
                    dados_d = []
                    if float(dados[2]) >= float(operacao[4]):
                        print('Saldo suficiente')
                        query = 'SELECT numero FROM conta'
                        cursor.execute(query)
                        consulta = cursor.fetchall()

                        for i in consulta:
                            print(i[0],'==',operacao[3])
                            if str(i[0]) == str(operacao[3]):
                                dados_d = i

                        print(dados[0],'==',operacao[3])
                        if str(dados_d[0]) == str(operacao[3]):
                            #Reduzir o saldo
                            print('O destino existe')
                            query = 'UPDATE conta SET saldo = saldo - %s WHERE numero = %s'
                            values = (operacao[4],operacao[2])
                            cursor.execute(query,values)
                            print('Chegou aqui')
                            data = datetime.now()
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                            query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                            values = (f'Transfência:{operacao[2]} para {operacao[3]} - Data:{data}',data,operacao[2])
                            cursor.execute(query,values)
                            print('Chegou nesse outro')
                            #Depositar o dinheiro da conta destinataria
                            query = 'UPDATE conta SET saldo = saldo + %s WHERE numero = %s'
                            values = (operacao[4],operacao[3])
                            cursor.execute(query,values)
                            data = datetime.now()
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                            query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                            values = (f'Deposito:{operacao[4]} de {operacao[2]} - Data:{data}',data,operacao[3])
                            cursor.execute(query,values)
                            query = 'SELECT saldo,numero FROM conta'
                            cursor.execute(query)
                            consulta = cursor.fetchall()
                            saldo = []
                            for i in consulta:
                                if i[1] == operacao[2]:
                                    saldo = i[0]
                            # 1 == Sucesso na operação
                            con.send(f'1,{saldo}'.encode())
                        else:
                            # 0 == Destino invalido
                            con.send('0'.encode())
                    else:
                        # 2 == Saldo insuficiente 
                        con.send('2'.encode())

    #           -------- EXTRATO --------
                elif operacao[0] == '5':
                    #Restante dos valores | 1 = numero
                    query = 'SELECT data,numero FROM historico'
                    cursor.execute(query)
                    consulta = cursor.fetchall()

                    lista = []
                    for i in consulta:
                        if i[1] == operacao[1]:
                            lista.append(i[0])
                    print(lista)
                    for i in lista:
                        con.send(f'{i}'.encode())
                        #Esse recebimento só serve como trava para o servidor não mandar todos os dados
                        #de uma vez e dar erro por excessode trafégo no lado do usuário 
                        con.recv(1024).decode()
                    con.send('1'.encode())

                elif operacao[0] == '6':
                    con.close()
                    break
            except:
                con.close()
                break

            print('Client at ',self.adress, ' disconnected...')



def gera_numero(lista):
    n = randint(100,999)

    for i in lista:
        if i[0] == n:
            return gera_numero(lista)
    return str(n)
    
host = '0.0.0.0'
port = 8000
addr = ((host,port))
conn = mysql.connector.connect(host='localhost',database='sysbank',user='root',password='')
cursor = conn.cursor()

socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
socket_server.bind(addr)
while(True): 
    socket_server.listen(30)
    print('Aguardando conexão...\n')
    con, cliente = socket_server.accept()
    newthread = usuario(cliente, con)#Talvez seja o contrario
    print('Conectado\n')
    