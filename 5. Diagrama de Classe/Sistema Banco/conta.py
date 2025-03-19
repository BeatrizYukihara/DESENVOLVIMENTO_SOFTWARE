from transacoes import Saque, Deposito

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    def ver_saldo(self):
        print(f'Seu saldo é {self.saldo}')

    def nova_conta(self, saldo, cliente, numero):
        return Conta(saldo, numero, self.agencia, cliente, self.historico)
    

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            print(f'Saque de R$ {valor} realizado com sucesso')

    def depositar(self, valor):
        if valor:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            print(f'Depósito de R$ {valor} realizado com sucesso')

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques
