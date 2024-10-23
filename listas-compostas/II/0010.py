N = int(input('Testes: '))

if N < 1 or N > 100:
    print('Valor inválido')

else:
    for i in range(N):
        numero = int(input(f'Número {i+1}: '))
        
        divisores = []
        for n in range(1, 100000000):
            if numero % n == 0 and n != numero:
                divisores.append(n)
                soma = sum(divisores)
                
        if soma == numero:
            print(f'{numero} é perfeito.')
        else:
            print(f'{numero} não é perfeito.')
