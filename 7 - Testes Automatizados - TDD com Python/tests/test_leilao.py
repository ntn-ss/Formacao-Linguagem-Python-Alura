from unittest import TestCase
from leilao.dominio import Usuario, Leilao, Lance
from leilao.excecoes import LanceInvalido
class TestLeilao(TestCase):
    # o método setUp é executado por padrão antes de qualquer outro teste. Preferir pôr apenas o que for comum a tudo, quiçá na menor quantidade possível, pois se forem códigos demais (ex.: instâncias de objetos), a máquina pode ficar lenta na execução de muitos testes.
    def setUp(self):
        self.nathan = Usuario('Nathan', 500.0)
        self.lance_do_nathan = Lance(self.nathan, 300.00)

        self.leilao = Leilao('Cinquentinha')
        self.leilao.propoe(self.lance_do_nathan)
    
    # primeiro caso de uso, ordem crescente.
    # alguns programadores gostam de nomear seus testes com a situação antes e o verbo depois.
    def test_deve_retornar_maior_e_menor_valor_de_lances_adicionados_em_ordem_crescente (self):
        
        breno = Usuario('Breno', 500.0)
        lance_do_breno = Lance(breno, 300.01)
        
        self.leilao.propoe(lance_do_breno)
        
        menor_valor_esperado = 300.00
        maior_valor_esperado = 300.01
        
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
        
        
    # segundo caso de uso, ordem decrescente.
    # este teste antes retornava os maiores e menores valores quando adicionados em ordem descrescente, mas essa ideia tornou-se defasada graças à regra de negócio adicionada mais abaixo no arquivo. isso é relativamente comum no "mundo real", os testes de software devem se adaptar às mudanças da corporação.
    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente (self):
        with self.assertRaises(LanceInvalido):
            breno = Usuario('Breno', 500.0)
            lance_do_breno = Lance(breno, 300.01)
            
            self.leilao.propoe(lance_do_breno)
            self.leilao.propoe(self.lance_do_nathan)
        
    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance (self):
                
        self.assertEqual(300.0,self.leilao.menor_lance)   
        self.assertEqual(300.0,self.leilao.maior_lance)
    
    # a partir daqui, torna-se inútil testar essa funcionalidade pois é tudo muito parecido e podemos ter confiança de que a quantidade de itens independe, salvo se houver uma regra de negócio como "lance de número X recebe bonificação".
    
    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances (self):
        thales = Usuario('Thales', 500.0)
        lance_do_thales = Lance(thales, 300.01)
        
        breno = Usuario('Breno', 500.0)
        lance_do_breno = Lance(breno, 300.02)

        self.leilao.propoe(lance_do_thales)
        self.leilao.propoe(lance_do_breno)
        
        menor_valor_esperado = 300.00
        maior_valor_esperado = 300.02
        
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
        
    '''
    novas regras de negócio:
    
    regra 1: se o leilão não tiver lances, deve permitir propor um lance.
    '''
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        # o setUp já propoe o lance_do_nathan.
        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebidos)
        
    # regra 2: se o último usuário for diferente, deve permitir propor um lance.
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        breno = Usuario("Breno", 500.0)
        lance_do_breno = Lance(breno, 400.0)
        
        self.leilao.propoe(lance_do_breno)
        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebidos)
    # regra 3: se o último usuário for o mesmo, deve negar propor um lance.
    def test_deve_negar_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_nathan_de_quatrocentos = Lance(self.nathan, 400.0)
        
        # se eu não lançasse uma exceção LanceInvalido no módulo dominio, este método retornaria "falso" e o teste falharia.
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(lance_do_nathan_de_quatrocentos)