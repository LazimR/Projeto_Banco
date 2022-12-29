

import datetime
from random import randint
class Conta:
    __slots__ = ['_numero','_titular','saldo','_limite','_historico','_senha','_login']
    
    _total_contas = 0
    
    
    def __init__(self,numero,titular,senha,login,saldo = 0 ,limite = 1000):
        self._numero = numero
        self._titular = titular
        self.saldo = saldo
        self._limite = limite
        self._historico = Historico()
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
    def get_limite(self):
        return self._limite
    
    @get_limite.setter
    def set_limite(self,l):
        self._limite = l

    @property
    def get_historico(self):
        return self._historico

    @get_historico.setter
    def set_historico(self,h):
        self._historico = h

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

def gera_numero(b):
    n = randint(100,999)
    for i in b.contas:
        if b.contas[i].get_numero == n:
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
