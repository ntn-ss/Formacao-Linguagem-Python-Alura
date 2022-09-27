import re

email1 = "Meu número é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular"
email4 = "lalalalalalalala 923851238 7325-4123 sahusauhsauhs 989765342"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao, email4)
print(retorno)