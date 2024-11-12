class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def atualizar_nome(self, nome):
        novo_nome = input("Digite o novo nome: ")
        self.nome = novo_nome
        
    def atualizar_idade(self, idade):
        nova_idade = input("Digite a nova idade: ")
        self.idade = int(nova_idade)

    def atualizar_peso(self, peso):
        novo_peso = input("Digite o novo peso: ")
        self.peso = float(novo_peso)
        
while True:
    nome = input('Nome: ')
    idade = int(input('Idade: ')
    peso = float(input('Peso: ')
    
    infos = Pessoa(nome, idade, peso) 
    
    att_infos = input('Deseja atualizar as informações? ').capitalize()
    if att_infos == 'Sim':
        infos.atualizar_nome()
        infos.atualizar_idade()
        infos.atualizar_peso()
        
    print(f'Nome: {infos.nome}')
    print(f'Idade: {infos.idade}')
    print(f'Peso: {infos.peso}')
    
    add_infos = input('Deseja adicionar informações? ').capitalize()
    if add_infos != 'Sim':
        break

