#estou estudando OOP e a medida dos treinos os códigos ficarão mais complexos e  organizados

class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudar(self):
        print(f"olá, meu nome é {self.nome} e tenho {self.idade}")


Usuario1 = Usuario("fernando", 12)
Usuario1.saudar()
