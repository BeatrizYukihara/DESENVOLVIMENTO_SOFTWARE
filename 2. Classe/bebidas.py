class Bebidas:
    def __init__(self, nome, preco, quantidade, ingredientes):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.ingredientes = ingredientes 

    def __str__(self):
        return f'A bebida {self.nome} custa R${self.preco}, contem {self.quantidade}mls e é feita com {self.ingredientes}'
    
    def desconto(self, percentual_desconto):
        if 0 < percentual_desconto < 100:
            desconto = self.preco * (percentual_desconto / 100)
            self.preco -= desconto
            print(f'O preço da bebida {self.nome} após {percentual_desconto}% de desconto é R${self.preco:.2f}')
        else:
            print('Desconto inválido. Deve ser entre 0 e 100.')

if __name__ == "__main__":
    bebida = Bebidas("coquetel de frutas", 35, 350, "laranja, abacaxi, morango e gelo",)
    print(bebida)
    bebida.desconto(50)