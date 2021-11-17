class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None ):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    lubawski = Pessoa(nome = 'Lubawski')
    nathan = Pessoa(lubawski, nome = 'Nathan')
    print(Pessoa.cumprimentar(nathan))
    print(id(nathan ))
    print(nathan.cumprimentar())
    print(nathan.nome)
    print(nathan.idade)
    for filho in nathan.filhos:
        print(filho.nome)
    nathan.sobrenome = 'teste' #criacao de atributo dinamico
    print(nathan.sobrenome)
    del lubawski.filhos # deletando atributo dinamicamente
    print(nathan.__dict__)   #verificar todos atributos de instancia
    print(lubawski.__dict__)


