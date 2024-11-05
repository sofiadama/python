traduçao = {'brasil': 'Feliz Natal!', 'alemanha': 'Frohliche Weihnachten!',
            'austria': 'Frohe Weihnacht!', 'coreia': 'Chuk Sung Tan!',
            'espanha': 'Feliz Navidad!', 'grecia': 'Kala Christougena!',
            'estados-unidos': 'Merry Christmas!', 'inglaterra': 'Merry Christmas!',
            'australia': 'Merry Christmas!', 'portugal': 'Feliz Natal!', 'suecia': 'God Jul!',
            'turquia': 'Mutlu Noeller', 'argentina': 'Feliz Navidad!', 'chile': 'Feliz Navidad!',
            'mexico': 'Feliz Navidad!', 'antardida': 'Merry Christmas!', 'canada': 'Merry Christmas!',
            'irlanda': 'Nollaig Shona Dhuit!', 'italia': 'Buon Natale!', 'libia': 'Buon Natale!',
            'siria': 'Milad Mubarak!', 'marrocos': 'Milad Mubarak!', 'japao': 'Merii Kurisumasu!'}

def mensagem_natal(pais):
    return traduçao.get(pais, 'País não encontrado')

while True:
    pais = input('País: ').lower()
    print(mensagem_natal(pais))
    
    print()
    add_informacoes = input('Deseja adicionar informações? ').upper()
    if add_informacoes != 'S':
        break
    print()
    
