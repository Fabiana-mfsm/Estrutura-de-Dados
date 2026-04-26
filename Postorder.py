class TreeNode:
    def __init__(self, dado):
        self.dado = dado
        self.filho_esquerdo = None
        self.filho_direito = None

    def inserir(self, valor):
        if valor == self.dado:
            return
        if valor < self.dado:
            if self.filho_esquerdo is None:
                self.filho_esquerdo = TreeNode(valor)
            else:
                self.filho_esquerdo.inserir(valor)
        else:
            if self.filho_direito is None:
                self.filho_direito = TreeNode(valor)
            else:
                self.filho_direito.inserir(valor)

    def travessia_pos_ordem(self):
        if self.filho_esquerdo is not None:
            self.filho_esquerdo.travessia_pos_ordem()
        if self.filho_direito is not None:
            self.filho_direito.travessia_pos_ordem()
        print(f"{self.dado}, ", end="")

class Tree:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = TreeNode(valor)
        else:
            self.raiz.inserir(valor)

    def travessia_pos_ordem(self):
        if self.raiz is not None:
            self.raiz.travessia_pos_ordem()
            print()


def main():
    tree = Tree()
    valores = [25, 20, 27, 15, 22, 26, 30, 29, 32]

    for v in valores:
        tree.inserir(v)
    tree.travessia_pos_ordem()

if __name__ == "__main__":
    main()