escolha = [['futebol', 0],['natacao', 0],['volei', 0],['basquete', 0]]

matricula = 'SIM'
while matricula == 'SIM':
    cadastro = []
    nome = input('Nome completo: ')
    qtd = int(input('Quantos esportes pretende fazer? '))
    cadastro.append(nome)
    cadastro.append(qtd)

    for i in range(qtd):
        modalidade = str(input('Em qual modalidade deseja matricular-se? '))
        
        for j in range(len(escolha)):
            if modalidade == escolha[j][0]:
                escolha[j][1] += 1
                
    matricula = input('Deseja continuar matriculando? ').upper()

print(cadastro)
for n in cadastro:
    if qtd > 1:
        desconto = []
        desconto.append(nome)

for y in range(len(desconto)):
    print(f'{y[0]} ganhou 50% de desconto na segunda modalidade!')

for esporte, alunos in escolha:
    print(f'{esporte.capitalize()}: {alunos} aluno(s)')
