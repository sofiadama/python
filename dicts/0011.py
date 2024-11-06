mensagem = {'ingles': 'Merry Christmas', 
            'portugues': 'Feliz Natal', 
            'espanhol': 'Feliz Navidad', 
            'alemao': 'Frohe Weihnachten', 
            'italiano': 'Buon Natale'}

traduçoes = int(input('Número de traduções: '))

def quantidade_e_informaçoes():
    info = []
    for _ in range(traduçoes):
        crianças = int(input('Número de crianças: '))

        if crianças < 1 and crianças > 100:
            break
        else:
            for _ in range(crianças):
                print()
                nome = input('Nome: ').title()
                lingua = input('Língua: ').lower()
                info.append(nome)
                info.append(lingua)

    return info

def mensagem_crianças(info):
    print()
    print('Traduções de "Feliz Natal":')
    
    for i in range(0, len(info), 2):
        nome = info[i]
        lingua = info[i+1]
        print()
        print(nome)
        print(mensagem.get(lingua, 'Idioma não encontrado.'))

info = quantidade_e_informaçoes()
mensagem_crianças(info)
