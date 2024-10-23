aritmetica = input('S ou M: ').upper()
tamanho = int(input())

elementos = []
coluna = 0
linha = 0
for i in range(tamanho):
    valor = float(input(f'Valor da coluna {coluna} da linha {linha+1}: '))
    coluna += 1
    linha += 1
    elementos.append(valor)
    
    if coluna > 10 and linha > 11:
        coluna = 0
        linha = 1

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
