from unittest import TestCase
from dominio import Usuario, Leilao, Lance, Avaliador

class TestAvaliador(TestCase):
    # o método setUp é executado por padrão antes de qualquer outro teste. Preferir pôr apenas o que for comum a tudo quantidade possível, pois se forem códigos demais (ex.: instâncias de objetos), a máquina pode ficar lenta.
    def setUp(self):
        self.nathan = Usuario('Nathan')
        self.lance_do_nathan = Lance(self.nathan, 300.00)

        self.leilao = Leilao('Cinquentinha')
        self.leilao.propoe(self.lance_do_nathan)
    
    # primeiro caso de uso, ordem crescente.
    # alguns programadores gostam de nomear seus testes com a situação antes e o verbo depois.
    def test_deve_retornar_maior_e_menor_valor_de_lances_adicionados_em_ordem_crescente (self):
        
        breno = Usuario('Breno')
        lance_do_breno = Lance(breno, 300.01)
        
        self.leilao.propoe(lance_do_breno)
        
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)
        
        menor_valor_esperado = 300.00
        maior_valor_esperado = 300.01
        
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
        
        
    # segundo caso de uso, ordem decrescente.
    def test_deve_retornar_maior_e_menor_valor_de_lances_adicionados_em_ordem_decrescente (self):
        breno = Usuario('Breno')
        lance_do_breno = Lance(breno, 300.01)
        
        self.leilao.propoe(lance_do_breno)
        self.leilao.propoe(self.lance_do_nathan)
        
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)
        
        menor_valor_esperado = 300.00
        maior_valor_esperado = 300.01
        
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
        
    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance (self):
                
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)
        
        self.assertEqual(300.0,avaliador.menor_lance)   
        self.assertEqual(300.0,avaliador.maior_lance)
    
    # a partir daqui, torna-se inútil testar essa funcionalidade pois é tudo muito parecido e podemos ter confiança de que a quantidade de itens independe, salvo se houver uma regra de negócio como "lance de número X recebe bonificação".
    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances (self):
        breno = Usuario('Breno')
        lance_do_breno = Lance(breno, 300.01)
        
        thales = Usuario('Thales')
        lance_do_thales = Lance(thales, 299.99)

        self.leilao.propoe(lance_do_breno)
        self.leilao.propoe(lance_do_thales)
        
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)
        
        menor_valor_esperado = 299.99
        maior_valor_esperado = 300.01
        
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)