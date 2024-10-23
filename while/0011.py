verificar = 'SIM'

while verificar == 'SIM':
    salario = float(input('Informe seu salário: R$ '))
    desconto = salario*0.11

    if desconto <= 320:
        print(f'Desconto previdenciário: R$ {desconto:.2f}')
    else: 
        taxa_desconto = (320/salario)*100
        print('Limite de desconto previdenciário atingido.')
        print(f'Taxa de desconto, referente ao valor de R$ 320,00: {taxa_desconto:.1f}%')

    print()
    verificar = input('Deseja continuar verificando? \n').upper()
    print()

else:
    print('Programa encerrado.')
