nomes_originais = {'Chaves', 'Kiko', 'Nhonho', 'Chiquinha', 'Jadson'}
ass_falsas = 0

alunos_frequentes = int(input('Alunos que frequentam a aula: '))
    
for _ in range(alunos_frequentes):
    nome = input('Nome: ')
    if nome not in nomes_originais:
        ass_falsas += 1

print(f'Número de assinaturas falsas: {ass_falsas}')
