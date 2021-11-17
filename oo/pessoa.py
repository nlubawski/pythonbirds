class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade


    def cumprimentar(self):
        return f'ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Lubawski')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = "Nathan"
    print(p.nome)

