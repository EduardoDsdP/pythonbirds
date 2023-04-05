class Pessoa:

    Olhos = 2
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
    Eduardo.sobrenome='dos Santos'
    del Eduardo.filhos
    print(Eduardo.__dict__)  #__dict__ mostra os atributos das instancias de um objeto. Conforme da pra ver no resulta, lista lado a lado todos os valores.
    print(eliza.__dict__)
    print(Pessoa.Olhos)
    print(Eduardo.Olhos)
    print(eliza.Olhos)
    print(id(Pessoa.Olhos), id(Eduardo.Olhos), id(eliza.Olhos))



