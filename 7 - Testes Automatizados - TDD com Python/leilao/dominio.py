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
        
        # estamos pegando, do módulo sys, que se integra ao sistema operacional, o menor valor que um float pode ter. Estamos fazendo o mesmo com o maior valor possível e declarando esses valores a maior_lance e menor_lance. Inicializando as variáveis assim, temos (quase) certeza de que qualquer valor maior ou menor oferecido no leilão será incluído e não quebrará as condições.
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max
    
    def propoe(self, lance: Lance):
        # verificar uma lista significa retornar falso se ele for vazio. Com um not, ela estiver vazia, retorna verdadeiro.
        if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise ValueError("Erro ao propor lance.")
    
    @property
    def lances(self):
        # chama-se "cópia rasa de lista", queremos impedir que classes externas modifiquem o vetor de lances diretamente.
        return self.__lances[:]