j, l = map(int,input('Coluna e linha: ').split())

matriz = []

for i in range(l):
    linha = list(map(float,input(f'Valores da linha {i+1}: ').split()))
    matriz.append(linha)
    
pares = []
for n in matriz[-1]:
    if n % 2 == 0:
        pares.append(n)
        
print(f'Soma dos elementos pares: {sum(pares)}')

# revisar
diagonal = []
coluna = 0
linha = 0     
for i in range(j):
    valor = float(input(f'Valor da coluna {coluna} da linha {linha+1}: '))
    coluna += 1
    linha += 1
    diagonal.append(valor)
    media = sum(diagonal) / len(diagonal)

diagonal_sec = []
coluna = j
linha = 0
for i in range(j):
    valor = float(input(f'Valor da coluna {coluna} da linha {linha+1}: '))
    coluna -= 1
    linha += 1
    diagonal_sec.append(valor)
    media_sec = sum(diagonal_sec) / len(diagonal_sec)

elementos = []
coluna = 1
linha = 0
for i in range(l):
    valor = float(input(f'Valor da coluna {coluna} da linha {linha+1}: '))
    coluna += 1
    linha += 1
    
    if coluna == j:
        linha = 0
        
    elementos.append(valor)
    media_elementos = sum(elementos) / len(elementos)

print(f'Média da diagonal principal: {media}')
print(f'Média da diagonal secundária: {media_sec}')
print(f'Média dos elementos acima da diagonal principal: {media_elementos:.1f}')
