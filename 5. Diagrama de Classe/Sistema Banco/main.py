from cliente import PessoaFisica, Historico
from conta import ContaCorrente
from transacoes import Deposito, Saque

if __name__ == "__main__":

    historico = Historico()
    cliente = PessoaFisica("Rua A, 123", 1, "111.111.111-11", "João", "11/11/1111")
    conta_corrente = ContaCorrente(1000, "12345-6", "0001", cliente, historico, 500, 3)

    #adicionar conta ao cliente
    cliente.adicionar_conta(conta_corrente)

    #ver saldo inicial
    conta_corrente.ver_saldo()


    deposito = Deposito(200) #instancia um deposito com valor de 200
    cliente.realizar_transacao(conta_corrente, deposito)
    conta_corrente.ver_saldo() #saldo depois do depósito

 
    saque = Saque(150)
    cliente.realizar_transacao(conta_corrente, saque)
    conta_corrente.ver_saldo() #saldo depois do saque

    #criando nova conta
    nova_conta = conta_corrente.nova_conta(0, cliente, '123456')
    cliente.adicionar_conta(nova_conta)

