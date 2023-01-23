

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

def gera_numero(lista):
    n = randint(100,999)

    for i in lista:
        if i[0] == n:
            return gera_numero(lista)
    return str(n)

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
    print('Conectado\n')
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

        except:
            con.close()
            break
