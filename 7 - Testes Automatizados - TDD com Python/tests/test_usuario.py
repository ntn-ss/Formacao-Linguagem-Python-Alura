from leilao.dominio import Usuario, Leilao
from leilao.excecoes import LanceInvalido

import pytest

# significa avisar ao Pytest que a função abaixo é algo que os testes precisam para serem executados
@pytest.fixture
def nathan():
    return Usuario('Nathan', 100)

@pytest.fixture
def leilao():
    return Leilao("Cinquentinha")
# executar o comando "pytest" pelo terminal estando na raiz da pasta 7
# com o pytest, podemos fazer testes com funções em vez de classes.
def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(nathan, leilao):
        
    nathan.propoe_lance(leilao, 50.0)
    
    assert nathan.carteira == 50.0
    
# este teste tem implementação praticamente idêntica ao acima, mas como são para finalidades diferentes, vale a pena manter ambos.
def test_deve_permitir_propor_lance_quando_valor_for_menor_que_o_da_carteira(nathan, leilao):
    
    nathan.propoe_lance(leilao, 1.0)
    
    assert nathan.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_for_igual_ao_da_carteira(nathan, leilao):
    
    nathan.propoe_lance(leilao, 100.0)
    
    assert nathan.carteira == 0

def test_deve_negar_lance_quando_o_valor_for_maior_que_o_da_carteira(nathan):
    with pytest.raises(LanceInvalido):
        leilao = Leilao("Ferrari")
        
        nathan.propoe_lance(leilao, 500.0)