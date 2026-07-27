class ContaBanc():
    def __init__(self, titulo, saldo):
        self.titulo = titulo
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f"Depósito de R${valor} realizado")


minhaconta = ContaBanc("Rodrigo", 1000.0)
minhaconta.depositar(100)

outraconta = ContaBanc("Maria", 2000.0)
outraconta.depositar(200)

print(minhaconta.saldo)
print(outraconta.saldo)