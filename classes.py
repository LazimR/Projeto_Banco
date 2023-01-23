

import datetime
from random import randint
import mysql.connector
import socket
import hashlib
from datetime import datetime

class Conta:
    __slots__ = ['_numero','_titular','saldo','_historico','_senha','_login']
    
    _total_contas = 0
    
    
    def __init__(self,numero,titular,senha,login,saldo = 0):
        self._numero = numero
        self._titular = titular
        self.saldo = saldo
        self._senha = senha
        self._login = login
        Conta._total_contas += 1

    @staticmethod
    def get_total_contas():
        return Conta._total_contas
    
    @property
    def get_numero(self):
        return self._numero

    @get_numero.setter
    def set_numero(self,n):
        self._numero = n

    @property
    def get_titular(self):
        return self._titular

    @get_titular.setter
    def set_titular(self,t):
        self._titular = t

    @property
    def get_senha(self):
        return self._senha
    
    @get_senha.setter
    def set_senha(self,s):
        self._senha = s

    @property
    def get_login(self):
        return self._login
    
    @get_login.setter
    def set_login(self,l):
        self._login = l

    def deposita(self,quantidade):
        if quantidade > 0:

            self.saldo += quantidade
            self._historico.transacao.append(f'Deposito:{quantidade} - Data:{datetime.datetime.now()}\n') 
            return True
        else:
            return False

    def saque(self,quantidade,senha,t = 0):
        if senha == self._senha and quantidade > 0 and quantidade <= self.saldo:
            self.saldo -= quantidade
            if t == 0:
                self._historico.transacao.append(f'Saque:{quantidade} - Data:{datetime.datetime.now()}\n')
            else:
                self._historico.transacao.append(f'Transferência:{quantidade} - Data:{datetime.datetime.now()}\n')
            return True
        
        else:
            return False

    def extrato(self):
        print(f'Conta:{self._numero}  Saldo:{self.saldo}')
        self._historico.transacao.append(f'Pedido de extrato as {datetime.datetime.now()}')
        

    def transfere(self,destino,quantidade,senha):
        if self.saque(quantidade,senha,1):
            return destino.deposita(quantidade)
        else:
            return False
        
class Cliente:
    def __init__(self,nome,cpf):
        self._nome = nome
        self._cpf = cpf

    @property
    def get_nome(self):
        return self._nome
    
    @get_nome.setter
    def set_nome(self,n):
        self._nome = n

    @property
    def get_cpf(self):
        return self._cpf
    
    @get_cpf.setter
    def set_cpf(self,cpf):
        self._cpf = cpf

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.now()
        self.transacao = []

    def imprime(self):
        extrato = (f'Data abertura: {self.data_abertura}\nTransações:\n')
        for i in self.transacao:
            extrato += i
        return extrato

def gera_numero(bd):
    n = randint(100,999)
    query = 'SELECT numero FROM conta WHERE numero = ' + str(n)
    bd.cursor.execute(query)
    aux = bd.cursor.fetchall()
    if  aux[0] == n:
        return gera_numero()
    return n

class Banco:

    def __init__(self):
        self.contas = {}
        self.clientes = {}

    def adiciona_conta(self,c,l):
        if not(l in self.contas):
            self.contas[l] = c
            return True 
        else:
            return False

    def adiciona_cliente(self,c,cpf):
        if not(cpf in self.clientes):
            self.clientes[cpf] = c
            return True
        else:
            return False
    
    def busca_conta(self,n):
        for i in self.contas:
            if str(self.contas[i].get_numero) == n:
                return self.contas[i]
        return None
        

def confirma_login(l,s,b):
    if l in b.contas:
        if b.contas[l].get_senha == s:
            return True
        else:   
            return False
    else:
        return False

host = '0.0.0.0'
port = 8000
addr = ((host,port))

while(True): 
    conn = mysql.connector.connect(host='localhost',database='sysbank',user='root',password='')
    cursor = conn.cursor()

    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    socket_server.bind(addr)

    socket_server.listen(10)
    print('Aguardando conexão...\n')
    con, cliente = socket_server.accept()

    while(True):
#       0 - Cadastro | 1 - Login | 2 - Deposito | 3 - Saque | 4 - Transferência | 5 - Extrato
        try:
            operacao = con.recv(1024).decode()
            operacao = operacao.split(',')

#           -------- CADASTRO --------
            if operacao[0] == '0':
                #restante dos valores | 1 == nome | 2 == cpf | 3 == login | 4 == senha
                query = f'SELECT cpf, login FROM conta WHERE cpf = {operacao[2]} OR login = '+operacao[3]
                cursor.execute(query)
                consulta = cursor.fetchall()
                lista_dados = []
                for i in consulta:
                    for j in i:
                        lista_dados.append(j)
                if not(operacao[2] in lista_dados or operacao[3] in lista_dados):
                    query = 'INSERT INTO conta (nome, cpf, numero, saldo, login, senha) VALUES (%s, %s, %s, %s, %s, MD5(%s))'
                    n = gera_numero()
                    cursor.execute(query,(operacao[1],operacao[2],n,'0',operacao[3],operacao[4]))
                    # 1 == Sucesso na operação
                    con.send(f'1,{n}'.encode())
                else:
                    # 0 == Login/CPF já em uso
                    con.send('0'.encode())

#           -------- LOGIN --------
            elif operacao[0] == '1':
                #restante dos valores | 1 == login | 2 == senha
                query = 'SELECT login,senha,nome,numero FROM conta WHERE login = '+operacao[1]
                cursor.execute(query)
                consulta = cursor.fetchone()
                if consulta[1] == operacao[2]:
                    # 1 == Sucesso na operação
                    con.send(f'1,{consulta[2]},{consulta[3]}'.encode())
                else:
                    # 0 == Senha/Login incorreto
                    con.send('0'.encode())

#           -------- DEPOSITO --------
            elif operacao[0] == '2':
                #restante dos valores | 1 == numero | 2 == quantidade
                if float(operacao[2]) > 0:
                    query = f'UPDATE conta SET saldo = saldo + {operacao[2]} WHERE numero = '+operacao[1]
                    cursor.execute(query)
                    data = datetime.now()
                    data = data.strftime('%Y-%m-%d %H:%M:%S')
                    query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                    cursor.execute(query,(f'Deposito:{operacao[2]} - Data:{data}',data,operacao[1]))
                    query = 'SELECT saldo FROM conta WHERE numero = '+operacao[1]
                    cursor.execute(query)
                    consulta = cursor.fetchone()
                    # 1 == Sucesso na operação
                    con.send(f'1,{consulta[0]}'.encode())
                else:
                    # 0 == Quantidade negativa/nula
                    con.send('0'.encode())

#           -------- SAQUE --------
            elif operacao[0] == '3':
                #restante dos valores | 1 == senha | 2 == numero | 3 == valor
                query = 'SELECT senha,numero,saldo FROM conta WHERE numero = '+operacao[2]
                cursor.execute(query)
                consulta = cursor.fetchone()
                if operacao[1] == consulta[0]:
                    if float(consulta[2]) >= float(operacao[3]):
                        query = f'UPDATE conta SET saldo = saldo - {[operacao[3]]} WHERE numero = '+operacao[2]
                        cursor.execute(query)
                        data = datetime.now()
                        data = data.strftime('%Y-%m-%d %H:%M:%S')
                        query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                        cursor.execute(query,(f'Saque:{operacao[3]} - Data:{data}',data,operacao[2]))
                        query = 'SELECT saldo FROM conta WHERE numero = '+operacao[2]
                        cursor.execute(query)
                        consulta = cursor.fetchone()
                        # 1 == Sucesso na operação
                        con.send(f'1,{consulta[0]}'.encode())
                    else:
                        # 2 == Saldo insuficiente
                        con.send('2'.encode())
                else:
                    # 0 == Senha incorreta
                    con.send('0'.encode())

#           -------- TRANSFERÊNCIA --------      
            elif operacao[0] == '4':
                #restante dos valores | 1 == senha | 2 == numero R. | 3 == numero D. | 4 == valor
                
                query = 'SELECT saldo FROM conta WHERE numero = '+operacao[2]
                cursor.execute(query)
                consulta = cursor.fetchone()
                if float(consulta[0]) >= float(operacao[4]):
                    query = 'SELECT numero FROM conta WHERE numero = '+operacao[3]
                    cursor.execute(query)
                    consulta = cursor.fetchone()
                    if consulta[0] == operacao[3]:
                        #Reduzir o saldo
                        query = f'UPDATE conta SET saldo = saldo - {operacao[4]} WHERE numero = '+operacao[2]
                        cursor.execute(query)
                        data = datetime.now()
                        data = data.strftime('%Y-%m-%d %H:%M:%S')
                        query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                        cursor.execute(query,(f'Transfência:{operacao[2]} para {operacao[3]} - Data:{data}',data,operacao[2]))     
                        #Depositar o dinheiro da conta destinataria
                        query = f'UPDATE conta SET saldo = saldo + {operacao[4]} WHERE numero = '+operacao[3]
                        cursor.execute(query)
                        data = datetime.now()
                        data = data.strftime('%Y-%m-%d %H:%M:%S')
                        query = 'INSERT INTO historico (id,operacao,data,numero) values(DEFAULT,%s,%s,%s)'
                        cursor.execute(query,(f'Deposito:{operacao[4]} de {operacao[2]} - Data:{data}',data,operacao[3]))
                        query = 'SELECT saldo FROM conta WHERE numero = '+operacao[2]
                        cursor.execute(query)
                        consulta = cursor.fetchone()
                        con.send(f'1,{consulta[0]}'.encode())
                    else:
                        # 0 == Destino invalido
                        con.send('0'.encode())
                else:
                    # 2 == Saldo insuficiente 
                    con.send('2'.encode())

#           -------- EXTRATO --------
            elif operacao[0] == '5':
                #Restante dos valores | 1 = numero
                query = 'SELECT data FROM historico WHERE numero = '+operacao[1]
                cursor.execute(query)
                consulta = cursor.fetchall()
                for i in consulta:
                    con.send(f'{i[0]}'.encode())
                    #Esse recebimento só serve como trava para o servidor não mandar todos os dados
                    #de uma vez e dar erro por excessode trafégo no lado do usuário 
                    con.recv(1024).decode()
                con.send('1'.encode())

        except:
            con.close()
            break