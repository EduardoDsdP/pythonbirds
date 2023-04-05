class Pessoa:
    def __init__(self, nome=None, idade=35, altura=1.90):   #essa linha se trata do comando de atributo de inicialização
        self.altura = altura
        self.idade = idade
        self.nome = nome   # e aqui uso o none para indicar que terei um campo sem valor atribuido a ele ainda.
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':

    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Eduardo'
    print(p.nome)
    print(p.idade)
    print(p.altura)
