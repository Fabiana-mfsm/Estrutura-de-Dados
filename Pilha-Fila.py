class Pilha:
    def __init__(self):
        self.dados = []
    def push(self, valor):
        self.dados.append(valor)
    def pop(self):
        if len(self.dados) > 0:
            return self.dados.pop()
        return None

class Fila:
    def __init__(self):
        self.dados = []
    def inserir(self, valor):
        self.dados.append(valor)
    def remover(self):
        if len(self.dados) > 0:
            return self.dados.pop(0)
        return None

continuar = "s"

while continuar.lower() == "s":
    print("\n" + "-"*20)
    frase = input("Digite uma frase: ")
    frase_limpa = ""
    for caractere in frase:
        if caractere.isalnum():
            frase_limpa += caractere.lower()

    if frase_limpa == "":
        print("-"*50)
        print("Você não digitou nada. Por favor, digite algo")
        print("-"*50)

    else:
        pilha = Pilha()
        fila = Fila()

        for letra in frase_limpa:
            pilha.push(letra)
            fila.inserir(letra)
        eh_palindromo = True
        continuar_comparacao = True

        while len(pilha.dados) > 0 and continuar_comparacao:
            topo = pilha.pop()
            inicio = fila.remover()

            if topo != inicio:
                eh_palindromo = False
                continuar_comparacao = False

        print("-"*40)
        if eh_palindromo:
            print("Resultado: isso é um pilíndromo")
        else:
            print("Resultado: isso não é um palíndromo")
        print("-"*40)

    continuar = input("Deseja continuar? (s/n): ")