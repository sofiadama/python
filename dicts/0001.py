infos = []
com_pets = list()
sem_pets = list()
qtd_pessoas = 0

while True:
    cadastro = {}
    cadastro['nome'] = input('Nome: ').capitalize()
    qtd_pessoas += 1
    cadastro['idade'] = int(input('Idade: '))
    cadastro['pets'] = input('Possui pet(s)? ').upper()

    infos.append(cadastro)
    
    if cadastro['pets'] == 'S':
        com_pets.append(cadastro['nome'])
    elif cadastro['pets'] == 'N':
        sem_pets.append(cadastro['nome'])
    else:
        while cadastro['pets'] != 'S' and cadastro['pets'] != 'N':
            cadastro['pets'] = input('Digite novamente (S ou N): ').upper()

    print()
    add_informacoes = input('Deseja adicionar informações? ').upper()
    if add_informacoes != 'S':
        break
    print()

def media_de_idades():
    total_idades = sum(cadastro['idade'] for cadastro in infos)
    return total_idades / len(infos)
    
print()
print(f'Pessoas cadastradas: {qtd_pessoas}')
print(f'Média de idade do grupo: {media_de_idades():.1f}')
print(f'Pessoas com pets: {com_pets}')
print(f'Pessoas sem pets: {sem_pets}')
