POO = []

for i in range(50):
    ANM = []
    print()
    nome = input('Nome: ')
    notas = []
    
    ANM.append(nome)
    ANM.append(notas)
    
    i = 0
    while len(notas) < 3:
        n = float(input(f'Nota {i+1}: '))
        i += 1
        notas.append(n)
        
    media = sum(notas) / len(notas)
    ANM.append(media)
    
    POO.append(ANM)
    print()
    print(POO)
    
