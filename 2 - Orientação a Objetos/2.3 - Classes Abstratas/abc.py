from abc import ABC #abstract base classes = classes que já existem na documentação cujos métodos podem ser reaproveitados

from collections.abc import MutableSequence
from numbers import Complex

class Playlist(MutableSequence):
    pass

class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__()

filmes = Playlist()
numeral = Numero()