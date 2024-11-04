num_traduçoes = int(input('Número de traduções: '))

mensagem = {'ingles': 'Merry Christmas', 'portugues': 'Feliz Natal', 'espanhol':
            'Feliz Navidad', 'alemao': 'Frohe Weihnachten', 'italiano': 'Buon Natale'}

i = 1
while i < num_traduçoes:
    num_crianças = int(input('Número de crianças: '))
    if num_crianças < 1 and num_crianças > 100:
        break
    
    info = []
    for i in range(num_crianças):
        nome = input('Nome: ')
        lingua = input('Língua: ')
        info.append(nome)
        info.append(lingua)
            
        print()
        for idioma in mensagem:
            if lingua == idioma:
                print(nome)
                print(mensagem[idioma])
                print()
