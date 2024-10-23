import random
jogos = int(input('Quantos jogos serão sorteados? '))

print()
print(f'Sorteando {jogos} jogos...')
print()

for i in range(jogos):
    lista = []
    while len(lista) < 6:
        numero = random.randint(1, 61)
        if numero not in lista:
            lista.append(random.randint(1,61))
        
    print(f'Jogo {i+1}: {lista}')
    
print()
print('Boa sorte!')
