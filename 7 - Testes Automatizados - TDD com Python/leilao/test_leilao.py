from unittest import TestCase
from dominio import Usuario, Leilao, Lance

class TestLeilao(TestCase):
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
        
        menor_valor_esperado = 300.00
        maior_valor_esperado = 300.01
        
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
        
        
    # segundo caso de uso, ordem decrescente.
    def test_deve_retornar_maior_e_menor_valor_de_lances_adicionados_em_ordem_decrescente (self):
        breno = Usuario('Breno')
        lance_do_breno = Lance(breno, 300.01)
        
        self.leilao.propoe(lance_do_breno)
        self.leilao.propoe(self.lance_do_nathan)
        
        menor_valor_esperado = 300.00
        maior_valor_esperado = 300.01
        
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
        
    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance (self):
                
        self.assertEqual(300.0,self.leilao.menor_lance)   
        self.assertEqual(300.0,self.leilao.maior_lance)
    
    # a partir daqui, torna-se inútil testar essa funcionalidade pois é tudo muito parecido e podemos ter confiança de que a quantidade de itens independe, salvo se houver uma regra de negócio como "lance de número X recebe bonificação".
    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances (self):
        breno = Usuario('Breno')
        lance_do_breno = Lance(breno, 300.01)
        
        thales = Usuario('Thales')
        lance_do_thales = Lance(thales, 299.99)

        self.leilao.propoe(lance_do_breno)
        self.leilao.propoe(lance_do_thales)
        
        menor_valor_esperado = 299.99
        maior_valor_esperado = 300.01
        
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
        
    '''
    novas regras de negócio:
    
    se o leilão não tiver lances, deve permitir propor um lance.
    '''
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        # o setUp já propoe o lance_do_nathan.
        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebidos)
        
    # se o último usuário for diferente, deve permitir propor um lance.
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        breno = Usuario("Breno")
        lance_do_breno = Lance(breno, 400.0)
        
        self.leilao.propoe(lance_do_breno)
        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebidos)
    # se o último usuário for o mesmo, deve negar propor um lance.
    def test_deve_negar_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_nathan_de_quatrocentos = Lance(self.nathan, 400.0)
        
        self.leilao.propoe(lance_do_nathan_de_quatrocentos)
        
        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebidos)