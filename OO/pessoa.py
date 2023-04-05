class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35, altura=1.90):   #essa linha se trata do comando de atributo de inicialização
        self.altura = altura
        self.idade = idade
        self.nome = nome   # e aqui uso o none para indicar que terei um campo sem valor atribuido a ele ainda.
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':


    eliza = Pessoa(nome='Eliza')
    Eduardo = Pessoa(eliza, nome='Eduardo')
    print(Pessoa.cumprimentar(Eduardo))
    print(id(Eduardo))
    print(Eduardo.cumprimentar())
    print(Eduardo.idade)
    print(Eduardo.altura)
    for filho in Eduardo.filhos:
        print(filho.nome)
