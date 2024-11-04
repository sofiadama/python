infos = []

while True:
    cadastro = {}
    cadastro['nome'] = input('Nome: ').capitalize()
    ano = int(input('Ano de nascimento: '))
    cadastro['idade'] = 2024 - ano 
    cadastro['CLT'] = int(input('Carteira de trabalho: '))

    infos.append(cadastro)
    
    clt = []
    if cadastro['CLT'] != 0:
        ano_contrataçao = int(input('Ano de contratação: '))
        salario = float(input('Salário: '))
        aposentadoria = ano_contrataçao - ano + 35
        
        clt.append(ano_contrataçao)
        clt.append(salario)
        clt.append(aposentadoria)
        
    cadastro['informações'] = clt

    print()
    add_informacoes = input('Deseja adicionar informações? ').upper()
    if add_informacoes != 'S':
        break
    print()

print()
print('Nome:',cadastro.get('nome'))
print('Idade:',cadastro.get('idade'))
print('CLT:',cadastro.get('CLT'))
####print('Informações de CLT:',cadastro.get('informações'))
