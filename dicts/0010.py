viagens = int(input('Número de viagens ao mercado: '))
prods_e_preços = {}
prods_e_quantidade = {}

def verificar_produtos():
    print()
    for _ in range(viagens):
        qtd_produtos = int(input('Quantidade de produtos disponíveis: '))
        print()
        for i in range(qtd_produtos):
            prods_e_preços['produto'] = input(f'{i+1}º produto e preço: ').lower()
            try:
                prods_e_preços['preço'] = float(prods_e_preços['produto'])
            except ValueError:
                prods_e_preços['preço'] = prods_e_preços['produto']

        escolher_produtos()
        
def escolher_produtos():
    print()
    qtd_compras = int(input('Quantos produtos deseja comprar? '))
    for i in range(qtd_compras):
        prods_e_quantidade['produto'] = input(f'{i+1}º produto e quantidade: ').lower()
        try:
            prods_e_quantidade['quantidade'] = int(prods_e_quantidade['produto'])
        except ValueError:
            prods_e_quantidade['quantidade'] = prods_e_quantidade['produto']

verificar_produtos()

resultado = {}
for produto in prods_e_preços:
    if produto in prods_e_quantidade:
        resultado[produto] = prods_e_preços[produto] * prods_e_quantidade[produto]

print(resultado)
print(f'Valor total: {sum(resultado)}')
