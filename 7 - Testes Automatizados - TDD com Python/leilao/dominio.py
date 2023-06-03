import sys

class Usuario:
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome

class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
    
    @property
    def lances(self):
        return self.__lances

class Avaliador:
    def __init__(self):
        # estamos pegando, do módulo sys, que se integra ao sistema operacional, o menor valor que um float pode ter. Estamos fazendo o mesmo com o maior valor possível e declarando esses valores a maior_lance e menor_lance. Inicializando as variáveis assim, temos (quase) certeza de que qualquer valor maior ou menor oferecido no leilão será incluído e não quebrará as condições.
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    # tipando parâmetro de função
    def avalia(self, leilao: Leilao):
        for lance in leilao.lances:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor