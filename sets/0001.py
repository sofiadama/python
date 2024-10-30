escolha = [['futebol', 0], ['natacao', 0], ['volei', 0], ['basquete', 0]]
matricula = 'SIM'
cadastros = []

while matricula == 'SIM':
    cadastro = {}
    nome = input('Nome completo: ')
    qtd = int(input('Quantos esportes pretende fazer? '))
    cadastro['nome'] = nome
    cadastro['modalidades'] = []
    
    for i in range(qtd):
        modalidade = input(f'{i+1}ª modalidade: ').lower()
        cadastro['modalidades'].append(modalidade)
        for j in range(len(escolha)):
            if modalidade == escolha[j][0]:
                escolha[j][1] += 1
    
    cadastros.append(cadastro)
    matricula = input('Deseja continuar matriculando? ').upper()

def verificar_desconto(cadastros):
    desconto = []
    for cadastro in cadastros:
        if len(cadastro['modalidades']) > 1:
            desconto.append(cadastro['nome'])
    return desconto

desconto = verificar_desconto(cadastros)
print()
for nome in desconto:
    print(f'{nome} ganhou 50% de desconto na segunda modalidade!')

print()
for esporte, alunos in escolha:
    print(f'{esporte.capitalize()}: {alunos} aluno(s)')

print()
print(f'Quantidade de pessoas cadastradas: {len(cadastros)}.')
