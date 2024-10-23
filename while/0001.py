sexo = input("Digite 'F' para feminino ou 'M' para masculino: ").upper()

while sexo != 'F' and sexo != 'M':
    sexo = input('Sexo inválido. Por favor, digite novamente: ').upper()

else:
    if sexo == 'F':
        print('Sexo feminino')
    elif sexo == 'M':
        print('Sexo masculino')
