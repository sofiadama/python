QTD = int(input('Quantidade de números na lista: '))
print()

if QTD < 1 or QTD > 1000:
    print('Valor inválido')
    
else:
    numeros = list(map(int,input(f'Números: ').split()))[:QTD]
        
    inteiros = [2,3,4,5]
    for n in inteiros:
        contagem = sum(1 for i in numeros if i % n == 0)
      
        print(f'Múltiplos de {n}: {contagem}')
      
