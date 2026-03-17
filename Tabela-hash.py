class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, chave, valor):
        novo = No(chave, valor)

        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo

    def exibir(self):
        atual = self.inicio
        while atual is not None:
            print(f"[{atual.chave} - {atual.valor}] -> ", end="")
            atual = atual.proximo
        print("None")

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave, valor):
        indice = self.hash(chave)

        if self.tabela[indice] is None:
            self.tabela[indice] = ListaEncadeada()

        self.tabela[indice].inserir(chave, valor)

    def exibir(self):
        for i in range(self.tamanho):
            print(f"Índice {i}: ", end="")
            if self.tabela[i] is not None:
                self.tabela[i].exibir()
            else:
                print("None")

if __name__ == "__main__":
    tabela = TabelaHash(5)

    print("Inserindo elementos na tabela...\n")

    tabela.inserir(1, "Chaulin matador de porco")
    tabela.inserir(6, "Martinho")
    tabela.inserir(11, "Zuquinha")

    tabela.inserir(2, "Natalino")
    tabela.inserir(7, "Joka")
    tabela.inserir(12, "Azanias")
    tabela.inserir(17, "Peu")
    tabela.inserir(5, "Biu") 
    tabela.inserir(4, "Zé")  

    print("Estado da tabela:\n")
    tabela.exibir()