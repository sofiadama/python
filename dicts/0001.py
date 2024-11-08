def cadastrar_pessoa():
    cadastro = {}
    cadastro['nome'] = input('NOME: ').title()
    cadastro['idade'] = int(input('IDADE: '))
    cadastro['pets'] = input('PETS (Sim/Não): ').capitalize()
    return cadastro

def verificar_posse_de_pets(cadastro, tem_pets, sem_pets):
    if cadastro['pets'] == 'Sim':
        tem_pets.append(cadastro['nome'])
    elif cadastro['pets'] == 'Não' or cadastro['pets'] == 'Nao':
        sem_pets.append(cadastro['nome'])

def media_de_idades(geral):
    soma_de_idades = sum(cadastro['idade'] for cadastro in geral)
    return soma_de_idades / len(geral)

def guardar_informaçoes(cadastro, geral):
    geral.append(cadastro)

def continuar_registros():
    add_informacoes = input('Deseja adicionar informações? ').capitalize()
    return add_informacoes == 'Sim'
    
geral = []
tem_pets = []
sem_pets = []

while True:
    cadastro = cadastrar_pessoa()
    verificar_posse_de_pets(cadastro, tem_pets, sem_pets)
    guardar_informaçoes(cadastro, geral)

    print()
    if not continuar_registros():
        break
    print()

print()
print(f'Pessoas cadastradas: {len(geral)}')
print(f'Média de idades: {media_de_idades(geral):.2f}')
print(f'Pessoas com pets: {tem_pets}')
print(f'Pessoas sem pets: {sem_pets}')
       
