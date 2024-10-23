cad = int(input('Quantidade de cadastros: '))
print()

NIP = []
pessoas = 0
for i in range(cad):
    info = []
    nome = input('Nome: ')
    pessoas += 1 
    idade = int(input('Idade: '))
    peso = float(input('Peso: '))
    print()
    info.append(nome)
    info.append(idade)
    info.append(peso)
    
    NIP.append(info)

for peso in info:
    if peso > 50:
        print(info)
    else:
        print(info)
    
NI = []
if idade > 20:
    NI.append(info)[:2]

print(NI)      
print(NIP)
print(f'Quantidade de pessoas cadastradas: {pessoas}.')
