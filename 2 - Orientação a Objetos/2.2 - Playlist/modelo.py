class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes


    def darLike(self):
        self._likes+=1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
onePiece = Serie("one piece", 1999, 23)
topGun = Filme("top gun - maverick", 2022, 140)
tMOC = Serie("todo mundo odeia o chris", 2006, 4)


vingadores.nome = "os vingadores"
vingadores.ano=2012
vingadores.duracao=120
vingadores.darLike()
onePiece.darLike()
onePiece.darLike()

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self,item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

filmesESeries = [vingadores, onePiece, topGun, tMOC]
playlistFimDeSemana = Playlist("fim de semana", filmesESeries)

print(f'Tamanho da playlist: {len(playlistFimDeSemana)}')

for programa in playlistFimDeSemana:
    print(programa)

print(f'Tá ou não tá? {onePiece in playlistFimDeSemana._programas}')