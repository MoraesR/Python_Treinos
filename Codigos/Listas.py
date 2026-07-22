import re
class FilaCircular:
    def __init__(self, tamanho):
        self.max_queue = tamanho
        self.items = [None] * self.max_queue
        # Inicializa ambos no último índice para que o primeiro elemento
        # inserido ocupe a posição 0 após o incremento [4]
        self.front = self.max_queue - 1
        self.rear = self.max_queue - 1

    def vazia(self):
        return self.front == self.rear

    def insere(self, x):
        self.rear = (self.rear + 1) % self.max_queue
        if self.rear == self.front:
            print("Erro: Estouro na fila")
            self.rear = (self.rear - 1 + self.max_queue) % self.max_queue
            return
        self.items[self.rear] = x

    def remove(self):
        if self.vazia():
            print("Erro: Underflow na fila")
            return None
        # Incremento circular do front antes de extrair o elemento [9]
        self.front = (self.front + 1) % self.max_queue
        return self.items[self.front]



if __name__ == "__main__":
    fila = FilaCircular(tamanho=5)

    fila.insere("x")
    fila.insere("C")
    fila.insere("X")
    fila.insere("X")

    print("Fila após inserir:", fila.items)
    print("Removido:", fila.remove())
    print("Fila após remover:", fila.items)
    print("Removido:", fila.remove())
  