linha = int(input('Linha: '))
aritmetica = input('S ou M: ').upper()

if linha > 11 and linha < 0:
    print('Valor inválido!')
    
else:
    elementos = []
    for j in range(12):
        valor = float(input(f'Valor da coluna {j} da linha {linha}: '))
        elementos.append(valor)

    def soma():
            return sum(elementos)
        
    def media():
            return sum(elementos) / len(elementos)
    print()
    print(f'Matriz: {elementos}')
    
    if aritmetica == 'S':
        resultado = soma()
        print(f'Soma: {resultado:.1f}')
        
    elif aritmetica == 'M':
        resultado = media()
        print(f'Média: {resultado:.1f}')
