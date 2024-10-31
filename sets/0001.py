esportes = [['futebol', 0], ['natação', 0], ['vôlei', 0], ['basquete', 0]]
infos = []

while True:
    cadastro = set()
    nome = input('Nome completo: ').capitalize()
    cadastro.add(nome)
    
    qtd = int(input('Quantos esportes pretende fazer? '))

    for i in range(qtd):
        modalidade = input(f'{i+1}ª modalidade: ').lower()
        cadastro.add(modalidade)

        for j in range(len(esportes)):
            if modalidade == esportes[j][0]:
                esportes[j][1] += 1

    infos.append(cadastro)

    print()
    matricular = input('Deseja continuar matriculando? ').upper()
    if matricular != 'S':
        break
    print()

def verificar_desconto(infos):
    desconto = []
    for cadastro in infos:
    if qtd > 1:
        for nome in range(len(infos)):
            desconto.append(nome)
            # arrumar 
    return desconto

desconto = verificar_desconto(infos)

print()
for nome in desconto:
    print(f'{nome} ganhou 50% de desconto na segunda modalidade!')

print()
for esporte, alunos in esportes:
    print(f'{esporte.capitalize()}: {alunos} aluno(s)')

print()
print(f'Quantidade de pessoas cadastradas: {len(infos)}.')
