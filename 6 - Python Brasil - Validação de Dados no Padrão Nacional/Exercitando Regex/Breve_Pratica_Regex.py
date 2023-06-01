# Encontrar a sequência "número - duas letras - número"

import re

# um número entre zero e nove, uma sequência de duas letras quaisquer, um número entre zero e nove.
regex_teste_1 = "[0-9][a-z]{2}[0-9]"
texto_teste_1 = "123 1aa2 1cc aa1"
resposta_teste_1 = re.search(regex_teste_1, texto_teste_1)
print(resposta_teste_1.group())

# Encontrar um e-mail terminado em @dominio.com.br

# qualquer sequência de letra ou número possuindo de cinco a cinquenta elementos, um arroba, qualquer sequência de letra ou número possuindo de três a dez elementos, um ponto, qualquer sequência de letra ou número possuindo de três a dez elementos.
regex_teste_2 = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto_teste_2 = "aaabbbccc nathan@gmail.com.br dseratgdhdsrze5t adsfgsdzagtfaedf"
resposta_teste_2 = re.search(regex_teste_2, texto_teste_2)
print(resposta_teste_2.group())

# telefone

telefone_molde = "(xx)yyyy-zzzz"
# duas vezes números quaisquer de zero a nove, de quatro a cinco vezes números quaisquer de zero a nove, quatro vezes números quaisquer de zero a nove.
telefone_regex = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto_telefone = "eu gosto do número 88999564821 e também gosto de 8592873329"
resposta_telefone = re.findall(telefone_regex, texto_telefone)
print(resposta_telefone)