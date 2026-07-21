class FilaCircular:
    def __init__(self, tamanho):
        self.max_queue = tamanho 
        self.item = [none] * self.max_queue
        # Inicializa ambos no último índice para que o primeiro elemento
        # inserido ocupe a posição 0 após o incremento [4]
        self.front = self.max_queue -1
        self.rear  = self.max_queue -1

    def vazia(self):
        return self.front == self.rear 

    def insere(self, x):
        self.rear = (self.rear + 1)% self.max_queue
        