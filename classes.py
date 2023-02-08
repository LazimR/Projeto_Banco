

import datetime
from random import randint
import mysql.connector
import socket
import threading
from datetime import datetime

class usuario(threading.Thread):
    def __init__(self,adress,con) -> None:
        threading.Thread.__init__(self)
        self.con = con
        self.adress = adress
        self.conn = mysql.connector.connect(host='localhost',database='sysbank',user='root',password='')
        self.cursor = self.conn.cursor()
        print('Nova conexao:',self.con)

    def run(self):
        while(True):
#       0 - Cadastro | 1 - Login | 2 - Deposito | 3 - Saque | 4 - Transferência | 5 - Extrato
            
            self.operacao = self.con.recv(1024)
            self.operacao = (self.operacao.decode()).split(',')

#           -------- CADASTRO --------
            if self.operacao[0] == '0':
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
    