class Pessoa:

    olhos = 2 #atributo de classe ou default, assim todos objetos usam ele e alocamos menos memoria

    def __init__(self, *filhos, nome=None, idade=None ):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    lubawski.olhos = 1
    print(nathan.__dict__)   #verificar todos atributos de instancia
    print(lubawski.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos) #atributo de classe voce acessa pela classe ou pelos objetos
    print(nathan.olhos)
    print(lubawski.olhos)
    print(id(Pessoa.olhos), id(nathan.olhos), id(lubawski.olhos))
    print(Pessoa.metodo_estatico(), nathan.metodo_estatico(), lubawski.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), nathan.nome_e_atributos_de_classe())



