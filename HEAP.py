class MaxHeap:
    def __init__(self):
        self.heap = []

    def remover(self, indice):
        if indice < 0 or indice >= len(self.heap):
            return None
        removido = self.heap[indice]
        self.heap[indice] = self.heap[-1]
        self.heap.pop()

        if indice < len(self.heap):
            self.descer(indice)
            return removido

    def descer(self, i):
        n = len(self.heap)
        esquerda = 2 * i + 1

        while esquerda < n:
            direita = 2 * i + 2
            maior = i

            if self.heap[esquerda] > self.heap[maior]:
                maior = esquerda

            if direita < n and self.heap[direita] > self.heap[maior]:
                maior = direita

            if maior == i:
                return

            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            i = maior
            esquerda = 2 * i + 1


heap = MaxHeap()
heap.heap = [50, 30, 40, 10, 20, 35]

print("Sequência antes:", heap.heap)
heap.remover(0)
print("Sequência depois:", heap.heap)