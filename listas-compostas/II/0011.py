testes = int(input('Testes: '))

if testes < 2 or testes > 1000:
    print('Valor inválido')
    
for _ in range(testes):
    qtd = int(input('Suspeitos: '))
    nivel_suspeita = list(map(int,input('Nível de suspeita: ').split()))[:qtd]
    
    if len(nivel_suspeita) < 2:
        print('Só há um suspeito.')
        
    else:
        primeiro = max(nivel_suspeita)
        segundo = max(i for i in nivel_suspeita if i != primeiro)
        posicao_segundo = nivel_suspeita.index(segundo)
        print(f'{posicao_segundo+1}ª posição.')
