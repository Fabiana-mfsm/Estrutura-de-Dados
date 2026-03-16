class Musica:
    def __init__(self, id, nome, artista):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.proximo = None
        self.anterior = None

class Playlist:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, id, nome, artista):
        nova = Musica(id, nome, artista)
        if self.inicio == None:
            self.inicio = nova
            self.fim = nova
        else:
            self.fim.proximo = nova
            nova.anterior = self.fim
            self.fim = nova

    def remover_inicio(self):
        if self.inicio == None:
            print("Lista vazia")
        else:
            print("Removendo:", self.inicio.nome)
            self.inicio = self.inicio.proximo
            if self.inicio != None:
                self.inicio.anterior = None

    def listar(self):
        atual = self.inicio
        while atual != None:
            print(atual.nome, "-", atual.artista)
            atual = atual.proximo

    def listar_reverso(self):
        atual = self.fim
        while atual != None:
            print(atual.nome, "-", atual.artista)
            atual = atual.anterior

playlist = Playlist()
playlist.adicionar(1, "Bohemian Rhapsody", "Queen")
playlist.adicionar(2, "Smells Like Teen Spirit", "Nirvana")
playlist.adicionar(3, "Rolling in the Deep", "Adele")
playlist.adicionar(4, "Shape of You", "Ed Sheeran")
playlist.adicionar(5, "Blinding Lights", "The Weeknd")

print("\nPlaylist normal:")
playlist.listar()

print("\nPlaylist reversa:")
playlist.listar_reverso()

atual = playlist.inicio
print("\nComeçou:", atual.nome)

atual = atual.proximo
print("Avançou:", atual.nome)

atual = atual.proximo
print("Avançou:", atual.nome)

atual = atual.anterior
print("Voltou:", atual.nome)

print("\nRemovendo primeira música")
playlist.remover_inicio()

print("\nPlaylist atualizada:")
playlist.listar()

# Resposta da reflexão: Por que uma lista duplamente encadeada é mais adequada para uma playlist do que uma lista simplesmente encadeada?
# RESPOSTA:
# Uma lista duplamente encadeada é mais adequada para uma playlist porque cada elemento fica duplamente ligado: um que aponta para o próximo nó e outro que aponta para o nó anterior.
# Em uma playlist geralmente se navega para frente e para trás percorrendo as músicas. A lista duplamente encadeada permite fazer esse tipo de navegação, pois está ligada ao nó anterior e posterior, permitindo assim uma navegação bidirecional, o ideal para uma playlist.