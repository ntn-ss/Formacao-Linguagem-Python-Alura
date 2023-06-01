# Eu poderia fazer tudo manualmente, mas é melhor usar esta ferramenta: https://pypi.org/project/validate-docbr/
from CpfCnpj import CpfCnpj
from TelefonesBr import TelefonesBr
from DatasBr import DatasBr
from AcessoCep import BuscaEndereco

exemplo_cnpj = '10341650000154'
exemplo_cpf = '91633608026'

documento = CpfCnpj(exemplo_cpf, "cpf")
documento2 = CpfCnpj(exemplo_cnpj, "cnpj")

print(documento)
print(documento2)

telefone = "558899481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

cadastro = DatasBr()
print(cadastro)
print(cadastro.tempo_cadastro())

cep = "07082400"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print (bairro, cidade, uf)