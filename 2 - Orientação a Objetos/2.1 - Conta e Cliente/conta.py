class Conta:
    
    #construtor
    def __init__(self, numero, titular, saldo, limite, codigobanco = 101):
        print("Construindo objeto... {}".format(self))
        
        #atributos
        #dois underscores em frente a um atributo significa "privado". Chama-se "encapsulamento". Diferente do Java e companhia, não há palavra-chave.
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #métodos
    def extrato(self):
        print("Saldo {} do titular {}.".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        if(self.__podeSacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite.".format(valor))

    def __podeSacar(self, valorASacar):
        valorDisponivelASacar = self.__saldo + self.__limite
        return valorASacar <= valorDisponivelASacar

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    #propriedades
    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigoBanco():
        return "001"

    @staticmethod
    def codigosBancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}