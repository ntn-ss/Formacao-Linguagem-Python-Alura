from unittest import TestCase
from dominio import Usuario, Leilao, Lance, Avaliador

class TestAvaliador(TestCase):
    # primeiro caso de uso, ordem crescente.
    def test_avalia(self):
        nathan = Usuario('Nathan')
        breno = Usuario('Breno')

        lance_do_nathan = Lance(nathan, 300.00)
        lance_do_breno = Lance(breno, 300.01)

        leilao = Leilao('Cinquentinha')

        leilao.lances.append(lance_do_nathan)
        leilao.lances.append(lance_do_breno)
        
        avaliador = Avaliador()
        avaliador.avalia(leilao)
        
        menor_valor_esperado = 300.00
        maior_valor_esperado = 300.01
        
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
        
        
    # segundo caso de uso, ordem decrescente.
    def test_avalia2(self):
        nathan = Usuario('Nathan')
        breno = Usuario('Breno')

        lance_do_breno = Lance(breno, 300.01)
        lance_do_nathan = Lance(nathan, 300.00)

        leilao = Leilao('Cinquentinha')

        leilao.lances.append(lance_do_breno)
        leilao.lances.append(lance_do_nathan)
        
        avaliador = Avaliador()
        avaliador.avalia(leilao)
        
        menor_valor_esperado = 300.00
        maior_valor_esperado = 300.01
        
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)