

from statsmodels.genmod.families.varfuncs import mu
class Musica: 
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
    
    def __str__(self):
        return f"{self.nome}" - {self.artista} - {self.duracao}"

Musica1 = Musica("Bohemian Rhapsody", "Queen", 354) 
musica2 = Musica("Imagine", "John Lennon", 183)

def main ()
    print(musica1)
    print(musica2)
