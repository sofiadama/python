infos = []
cadastro = {}
clt = {}

def informacoes_clt():
    
    if cadastro['CLT'] != 'Não':
        clt['ano_contrataçao'] = int(input('Ano de contratação: '))
        clt['salario'] = float(input('Salário: R$ '))
        clt['aposentadoria'] = clt['ano_contrataçao'] - ano + 35
        
    cadastro['informações'] = clt

while True:

    cadastro['pessoa'] = input('Nome: ').title()
    ano = int(input('Ano de nascimento: '))
    cadastro['idade'] = 2024 - ano 
    cadastro['CLT'] = input('Carteira de trabalho (Sim/Não): ').capitalize()

    infos.append(cadastro)

    print()
    informacoes_clt()

    print()
    print('Nome:',cadastro.get('pessoa'))
    print('Idade:',cadastro.get('idade'))
    print('CLT:',cadastro.get('CLT'))
    print()
    print('INFORMAÇÕES DA CLT')
    print('Ano de contratação:',clt.get('ano_contrataçao'))
    print('Salário: R$',clt.get('salario'))
    print('Idade de aposentadoria:',clt.get('aposentadoria'),'anos')

    print()
    add_info = input('Deseja adicionar informações? ').upper()
    if add_info != 'S':
        break
    print()
