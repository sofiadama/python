class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def atualizar_nome(self, novo_nome):
        self.nome = novo_nome
        
    def atualizar_idade(self, nova_idade):
        self.idade = nova_idade

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso

def obter_nome():
    return input('NOME: ').title()

def obter_idade():
    while True:
        try:
            idade = int(input('IDADE: '))
            return idade
        except ValueError:
            print('A idade deve ser um valor inteiro.')

def obter_peso():
    return float(input('PESO: ')) 

def deseja_atualizar():
    atualizar = input('Deseja atualizar as informações? ').strip().capitalize() 
    return atualizar == 'Sim'

def deseja_adicionar():
    adicionar = input('Deseja adicionar cadastro? ').strip().capitalize()
    return adicionar == 'Sim'

def imprimir_informaçoes(infos):
    print(f'NOME: {infos.nome}')
    print(f'IDADE: {infos.idade} anos')
    print(f'PESO: {infos.peso:.2f} kg')
    
def main():        
    while True:
        nome = obter_nome()
        idade = obter_idade()
        peso = obter_peso()
    
        infos = Pessoa(nome, idade, peso) 

        print()
        if deseja_atualizar():
            print()
            novo_nome = input('NOVO NOME: ')
            infos.atualizar_nome(novo_nome)

            nova_idade = int(input('NOVA IDADE: '))
            infos.atualizar_nome(nova_idade)

            novo_peso = float(input('NOVO PESO: '))
            infos.atualizar_peso(novo_peso)

        print()
        imprimir_informaçoes(infos)

        print()
        if not deseja_adicionar():
            break
        print()

if __name__ == '__main__':
    main()
    
