

import datetime
from random import randint
import mysql.connector
import socket
import threading
from datetime import datetime

class usuario(threading.Thread):

    """
    Essa classe representa um cliente

    Atributos
    ---------------
    adress : objeto
    É o endereço da maquina do usuário
    
    con : objeto
    É a conexão do cliente com o servidor
    
    conn : objeto
    É a conexão com o banco de dados

    cursor: objeto
    É um objeto que é instaciado da conexão, servindo para fazer consultas SQL

    Metodos
    ---------------

    run():
        Essa função possui um laço while que vai ficar processando a conexão do usuário,
        recebendo seus pedidos e retornando o que precisa. Até que a conexão seja encerrada

    """

    def __init__(self,adress,con) -> None:
        threading.Thread.__init__(self)
        self.con = con
        self.adress = adress
        self.conn = mysql.connector.connect(host='localhost',database='sysbank',user='root',password='')
        self.cursor = self.conn.cursor()
        print('Nova conexao:',self.con)
    """
    Na função __init__ ela inicializa nossos atributos e recebe os atributos e funções da classe Thread
    Printando que a conexão foi feita e com qual usuário.
    """

    def run(self):
        while(True):
#       0 - Cadastro | 1 - Login | 2 - Deposito | 3 - Saque | 4 - Transferência | 5 - Extrato
            """
            Nessa parte da função ela vai ficar recebendo e tratando a mensagem que o usuário enviar,
            que vai ser composta basicamente de (nº da operação, valores restantes para a operação)
            """
            self.operacao = self.con.recv(1024)
            self.operacao = (self.operacao.decode()).split(',')
            
#           -------- CADASTRO --------
            if self.operacao[0] == '0':
                """
                Nessa parte o programa irá fazer uma pesquisa SQL recebendo todos os usuários do 
                nosso BD(banco de dados), logo em seguida ele irá filtrar a retorno da consulta, para
                verificar se os dados do usuário ja existem no BD, caso contrario ele continua a
                operação.

                O programa chama a função gera_numero e depois cadastra o nosso usuário no BD
                e envia uma mensagem com o valor 1 e o número da conta do usuário.

                No caso do usuário ja estar cadastrado, o programa envia um mensagem com o valor 0. 
                """
                print('Cadastro\n')
                #restante dos valores | 1 == nome | 2 == cpf | 3 == login | 4 == senha
                self.query = 'SELECT cpf, login FROM conta'
                self.cursor.execute(self.query)
                self.consulta = self.cursor.fetchall()
                self.dados = []
                for i in self.consulta:
                    if i[0] == self.operacao[2] or i[1] == self.operacao[3]:
                        self.dados = i

                if len(self.dados) == 0:
                    self.query = 'SELECT numero FROM conta'
                    self.cursor.execute(self.query)
                    self.aux = self.cursor.fetchall()
                    self.n = gera_numero(self.aux)

                    self.query = 'INSERT INTO conta (nome, cpf, numero, saldo, login, senha) VALUES (%s, %s, %s, %s, %s, %s)'
                    self.values = (self.operacao[1],self.operacao[2],self.n,'0',self.operacao[3],self.operacao[4])
                    self.cursor.execute(self.query,self.values)
                    # 1 == Sucesso na operação
                    self.con.send(f'1,{self.n}'.encode())
                else:
                    # 0 == Login/CPF já em uso
                    self.con.send('0'.encode())

#           -------- LOGIN --------
            elif self.operacao[0] == '1':
                """
                Nessa parte da função o programa faz uma consulta SQL para pegar os dados de 
                usuários cadastrados e então verifica se os dados recebidos são iguais a algum do nosso 
                BD, se for, ele envia uma mensagem com 1, nome do usuário, nº da conta e o saldo.

                Caso os dados não correspondam ele envia a mensagem com 0. 
                """
                print('Login')
                #restante dos valores | 1 == login | 2 == senha
                self.query = 'SELECT login,senha,nome,numero,saldo FROM conta'
                self.cursor.execute(self.query)
                self.consulta = self.cursor.fetchall()
                self.dados = []
                for i in self.consulta:
                    if i[0] == self.operacao[1]:
                        self.dados = i
                if self.dados[1] == self.operacao[2]:
                    # 1 == Sucesso na operação
                    self.con.send(f'1,{self.dados[2]},{self.dados[3]},{self.dados[4]}'.encode())
                else:
                    # 0 == Senha/Login incorreto
                    self.con.send('0'.encode())

#           -------- DEPOSITO --------
            elif self.operacao[0] == '2':
                """
                Nessa parte, primeiramente ele verifica se a quantia é maior que 0, se sim,
                nosso programa faz uma consulta SQL, atualizando o saldo da conta do usuário e
                inserindo essa operação no historico, e envia uma mensagem com 1 e o saldo atual.

                Caso o número não seja maior que 0, o programa envia uma mensagem com 0.
                """
                print('Deposito')
                #restante dos valores | 1 == numero | 2 == quantidade
                if float(self.operacao[2]) > 0:
                    self.query = 'UPDATE conta SET saldo = saldo + %s WHERE numero = %s'
                    self.values = (self.operacao[2],self.operacao[1])
                    self.cursor.execute(self.query,self.values)
                    data = datetime.now()
                    data = data.strftime('%Y-%m-%d %H:%M:%S')
                    self.query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                    self.values = (f'Deposito:{self.operacao[2]}R$ - Data:{data}',data,self.operacao[1])
                    self.cursor.execute(self.query,self.values)
                    self.query = 'SELECT saldo,numero FROM conta'
                    self.cursor.execute(self.query)
                    self.consulta = self.cursor.fetchall()
                    saldo = []
                    for i in self.consulta:
                        if str(i[1]) == str(self.operacao[1]):
                            saldo = i[0]

                    # 1 == Sucesso na operação
                    self.con.send(f'1,{saldo}'.encode())
                else:
                    # 0 == Quantidade negativa/nula
                    self.con.send('0'.encode())

#           -------- SAQUE --------
            elif self.operacao[0] == '3':
                """
                Nessa parte do codigo o programa faz uma consulta SQL recebendo a senha,numero e saldo
                de todas as contas do BD, depois filtra os dados, ficando apenas os dados do nosso
                usuário. Em seguida o programa faz outra consulta SQL, reduzindo o valor do saldo no
                BD e logo após inserindo essa operação no historico. E por fim envia uma mensagem com 1 
                e o saldo atual da conta.

                Caso a quantidade do saque seja maior que o saldo na conta o programa envia uma
                mensagem com 2.

                Caso a senha esteja incorreta o programa envia uma mensagem com 0.
                """
                print('Saque')
                #restante dos valores | 1 == senha | 2 == numero | 3 == valor
                self.query = 'SELECT senha,numero,saldo FROM conta'
                self.cursor.execute(self.query)
                self.consulta = self.cursor.fetchall()
                
                self.dados = []
                for i in self.consulta:
                    if str(i[1]) == str(self.operacao[2]):
                        self.dados = i

                if str(self.operacao[1]) == str(self.dados[0]):
                    if float(self.dados[2]) >= float(self.operacao[3]):
                        self.query = 'UPDATE conta SET saldo = saldo - %s WHERE numero = %s'
                        self.values = (self.operacao[3],self.operacao[2])
                        self.cursor.execute(self.query,self.values)
                        data = datetime.now()
                        data = data.strftime('%Y-%m-%d %H:%M:%S')
                        self.query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                        self.cursor.execute(self.query,(f'Saque:{self.operacao[3]}R$ - Data:{data}',data,self.operacao[2]))
                        self.query = 'SELECT saldo,numero FROM conta'
                        self.cursor.execute(self.query)
                        self.consulta = self.cursor.fetchall()
                        saldo = []
                        for i in self.consulta:
                            if str(i[1]) == str(self.operacao[2]):
                                saldo = i[0]
                        # 1 == Sucesso na operação
                        self.con.send(f'1,{saldo}'.encode())
                    else:
                        # 2 == Saldo insuficiente
                        self.con.send('2'.encode())
                else:
                    # 0 == Senha incorreta
                    self.con.send('0'.encode())

#           -------- TRANSFERÊNCIA --------      
            elif self.operacao[0] == '4':
                """
                Nessa condição o programa faz um consulta SQL, para receber os dados de todos os 
                usuários, depois ele filtra para permanecer apenas os dados do nosso usuário.
                Após isso ele faz outra consulta para receber o número de todos os usuários, se o 
                número do destinatário existir no nosso banco o programa continua a operação.
                Em seguida ele reduz o saldo da conta do nosso usuário e inseri essa operação no
                historico, após isso ele aumenta o saldo do destinatário e inseri essa operação no
                historico. E então o programa envia uma mensagem com 1 e o saldo atual da conta do
                nosso usuário.

                Caso o destinatário não exista, o programa envia uma mensagem 0.

                Caso a senha esteja incorreta, o programa envia uma mensagem 2.
                """
                #restante dos valores | 1 == senha | 2 == numero R. | 3 == numero D. | 4 == valor
                
                self.query = 'SELECT senha,numero,saldo FROM conta'
                self.cursor.execute(self.query)
                self.consulta = self.cursor.fetchall()
                
                self.dados = []
                for i in self.consulta:
                    if str(i[1]) == str(self.operacao[2]):
                        self.dados = i
                self.dados_d = []
                if float(self.dados[2]) >= float(self.operacao[4]):
                    self.query = 'SELECT numero FROM conta'
                    self.cursor.execute(self.query)
                    self.consulta = self.cursor.fetchall()

                    for i in self.consulta:
                        if str(i[0]) == str(self.operacao[3]):
                            self.dados_d = i

                    if str(self.dados_d[0]) == str(self.operacao[3]):
                        #Reduzir o saldo
                        self.query = 'UPDATE conta SET saldo = saldo - %s WHERE numero = %s'
                        self.values = (self.operacao[4],self.operacao[2])
                        self.cursor.execute(self.query,self.values)
                        data = datetime.now()
                        data = data.strftime('%Y-%m-%d %H:%M:%S')
                        self.query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                        self.values = (f'Transfência:{self.operacao[4]}R$ para {self.operacao[3]} - Data:{data}',data,self.operacao[2])
                        self.cursor.execute(self.query,self.values)
                        #Depositar o dinheiro da conta destinataria
                        self.query = 'UPDATE conta SET saldo = saldo + %s WHERE numero = %s'
                        self.values = (self.operacao[4],self.operacao[3])
                        self.cursor.execute(self.query,self.values)
                        data = datetime.now()
                        data = data.strftime('%Y-%m-%d %H:%M:%S')
                        self.query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                        self.values = (f'Deposito:{self.operacao[4]}R$ de {self.operacao[2]} - Data:{data}',data,self.operacao[3])
                        self.cursor.execute(self.query,self.values)
                        self.query = 'SELECT saldo,numero FROM conta'
                        self.cursor.execute(self.query)
                        self.consulta = self.cursor.fetchall()
                        saldo = []
                        for i in self.consulta:
                            if str(i[1]) == str(self.operacao[2]):
                                saldo = i[0]
                        # 1 == Sucesso na operação
                        self.con.send(f'1,{saldo}'.encode())
                    else:
                        # 0 == Destino invalido
                        self.con.send('0'.encode())
                else:
                    # 2 == Saldo insuficiente 
                    self.con.send('2'.encode())

#           -------- EXTRATO --------
            elif self.operacao[0] == '5':
                """
                Nessa ultima operação, o programa faz uma consulta SQL pegando todas a informações
                do historico, em seguida ele filtra para ficar apenas os dados refentes ao nosso 
                usuário, logo após ele irá ficar mandando mensagens para o usuário com cada 
                uma da operações do historico, até que lista com os dados do historico esteja
                vazia. E por fim ele envia uma mensagem com 1.
                """
                print('Extrato')
                #Restante dos valores | 1 = numero
                self.query = 'SELECT operacao,numero FROM historico'
                self.cursor.execute(self.query)
                self.consulta = self.cursor.fetchall()
                lista = []
                for i in self.consulta:
                    if str(i[1]) == str(self.operacao[1]):
                        lista.append(i[0])
                for i in lista:
                    self.con.send(f'{i}'.encode())
                    #Esse recebimento só serve como trava para o servidor não mandar todos os self.dados
                    #de uma vez e dar erro por excessode trafégo no lado do usuário
                    a = self.con.recv(1024).decode()
                self.con.send('1'.encode())
                

            elif self.operacao[0] == '6':
                self.con.close()
                break
        print('Client at ',self.adress, ' disconnected...')

            



def gera_numero(lista):
    n = randint(100,999)

    for i in lista:
        if i[0] == n:
            return gera_numero(lista)
    return str(n)
    
HOST = '0.0.0.0'
PORT = 8000
addr = ((HOST,PORT))


socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
socket_server.bind(addr)

while(True): 
    socket_server.listen(30)
    print('Aguardando conexão...\n')
    con, cliente = socket_server.accept()
    newthread = usuario(cliente,con)#Talvez seja o contrario
    newthread.start()
    print('Conectado\n')
    