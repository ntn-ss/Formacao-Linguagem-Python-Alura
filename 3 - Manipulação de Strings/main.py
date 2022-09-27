from extratorArgumentosURL import ExtratorArgumentosURL

'''

argumento = "https://bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=2000"

.............012345678910
subString = argumento[8:15]
print(subString)


argumento = "moedaorigem=real"
listaArgumentos = argumento.split("=")
subString = argumento[index + 1 :]
print(subString)

argumento = "moedaorigem = real"
listaArgumentos = argumento.split("=")
print(listaArgumentos)

string = 0

if (string):
    print("Tem algo aqui.")
else:
    print("Não tem algo aqui.")
'''

url = "https://bytebank.com.br/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=2000"

argumentosURL = ExtratorArgumentosURL(url)
moedaOrigem, moedaDestino = argumentosURL.extraiArgumentos()
valor = argumentosURL.extraiValor()
print(moedaOrigem, moedaDestino, valor)
print(argumentosURL)

argumentosURL2 = ExtratorArgumentosURL(url)
print(argumentosURL==argumentosURL2)


'''index = url.find("moedadestino") + len("moedadestino") + 1
substring = url[index:]
print(substring)'''

'''string = "bytebank"
stringNova = string.replace("byte", "nathan", 1)
print(stringNova)'''

''' banco1 = "bytebank"
banco2 = "Bytebank".lower()

urlByteBank = "https://bytebank.com"
url1        = "https://buscasites.com/busca?q=https://bytebank.com"
url2        = "https://bitebanco.com.br"
url3        = "https://bytebank.com/cambio/teste/teste"

print(url1.startswith(urlByteBank))'''