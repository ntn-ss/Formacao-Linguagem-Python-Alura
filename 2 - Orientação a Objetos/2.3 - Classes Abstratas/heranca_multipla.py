class Estudante:
    def __init__(self, nome):
        self.nome=nome

    def registraHoras(self, horas):
        print (f'Assistiu {horas} horas de aula...')
    
    def mostrarTarefas(self):
        print('Fez muitas tarefas...')
    
class UFC(Estudante):
    def mostrarTarefas(self):
        print('Fez muitas tarefas, aluno UFC')

    def buscaEstagiosDoMes(self, mes=None):
        print(f'Mostrando estágios - {mes}' if mes else 'Mostrando estágios deste mês')

class IFCE(Estudante):
    def mostrarTarefas(self):
        print('Fez muitas tarefas, aluno IFCE')
    
    def buscaSeminariosDoMes(self, mes=None):
        print(f'Mostrando seminários - {mes}' if mes else 'Mostrando seminários deste mês')


#MixIn
class Hippie:
    def __str__(self):
        return f'{self.nome} é um hippie'

class EnsinoMedio(IFCE, Hippie):
    pass

class Bacharel(UFC, IFCE, Hippie):
    pass

zeze = EnsinoMedio("Zezé")
zeze.mostrarTarefas()
zeze.buscaSeminariosDoMes()

# MRO
# Bacharel > UFC > IFCE > Estudante

breno = Bacharel("Breno")
breno.mostrarTarefas()
breno.buscaEstagiosDoMes()
breno.buscaSeminariosDoMes()
print(zeze)
print(breno)