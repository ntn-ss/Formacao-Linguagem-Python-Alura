from leilao.excecoes import LanceInvalido

class Usuario:
    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira
    
    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_e_valido(valor):
            raise LanceInvalido("Não pode propor lance com valor maior que o presente na carteira.")
        
        lance = Lance(self, valor)
        # se a proposição não funcionar, a linha de subtrair da carteira nem funciona
        leilao.propoe(lance)
        
        self.__carteira -= valor
    
    def _valor_e_valido(self, valor):
        return valor <= self.carteira

class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        
        self.maior_lance = 0.0
        self.menor_lance = 0.0
    
    def propoe(self, lance: Lance):
        # verificar uma lista significa retornar falso se ele for vazio. Com um not, ela estiver vazia, retorna verdadeiro.
        if self._lance_e_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor
            
            self.maior_lance = lance.valor
            
            self.__lances.append(lance)
    

    # criar métodos privados para conter condições de ifs ajuda muito na legibilidade
    def _tem_lances(self):
        return self.__lances

    def _sao_usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        else:
            raise LanceInvalido("O mesmo usuário não pode propor dois lances seguidos.")

    def _valor_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        else:
            raise LanceInvalido("O valor do lance atual deve ser maior que o do lance anterior.")

    def _lance_e_valido(self, lance):
        return not self._tem_lances() or (
            self._sao_usuarios_diferentes(lance) and
            self._valor_maior_que_lance_anterior(lance))

    @property
    def lances(self):
        # chama-se "cópia rasa de lista", queremos impedir que classes externas modifiquem o vetor de lances diretamente.
        return self.__lances[:]