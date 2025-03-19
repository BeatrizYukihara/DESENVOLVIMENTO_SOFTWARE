from conta import Conta
from transacoes import Transacao, Deposito, Saque

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)


class Cliente:
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        if isinstance(transacao, Deposito):
            conta.depositar(transacao.valor)
        elif isinstance(transacao, Saque):
            conta.sacar(transacao.valor)
        conta.historico.adicionar_transacao(transacao)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)
        print('Nova conta adicionada!')


class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento):
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
