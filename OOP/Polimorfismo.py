class Carros():
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor
    def descricao(self):
        print(f'O carro: {self.nome} é {self.cor}')

class Gol(Carros):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)

class Corsa(Carros):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)


gol1 = Gol('Corsinha', 'branco')
corsa1 = Corsa('Corsa', 'preto')

print(gol1.descricao())
print(gol1.nome)
print(gol1.cor)