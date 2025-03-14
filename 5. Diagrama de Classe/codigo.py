from abc import ABC, abstractmethod

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico: Historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia 
        self.cliente = cliente
        self.historico = historico 

    def saldo(self):
        pass

    def nova_conta(self, cliente: Cliente, numero):
        pass

    def sacar(self, valor): 
        pass

    def depositar(self, valor): 
        pass


class Transacao(ABC):
    @abstractmethod
    def registrar(conta):
        pass


class Cliente:
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        pass

    def adicionar_conta(conta: Conta):
        pass


class Historico:
    def adicionar_transacao(self, transacao: Transacao):
        pass
    
  
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico: Historico, limite, limite_saques):
        super().__init__(self, saldo, numero, agencia, cliente, historico: Historico)
        self.limite = limite
        self.limite_saques = limite_saques


class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super().__init__(self, endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(conta: Conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(conta: Conta):
        pass
