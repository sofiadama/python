def verificar_viagens():
    return int(input('Número de viagens ao mercado: '))

def verificar_produtos():
    return int(input('Quantidade de produtos disponíveis: '))
        
def escolher_produtos():
    return int(input('Quantos produtos deseja comprar? '))

def registrar_produtos():
    prods_e_preços['produto'] = input(f'{i+1}º produto: ').lower()
    prods_e_preços['preço'] = float(input('Preço: R$ '))

def registrar_compras():
    prods_e_quantidade['produto'] = input(f'{i+1}º produto: ').lower()
    prods_e_quantidade['quantidade'] = int(input('Quantidade: '))

viagens = verificar_viagens()
prods_e_preços = {}
prods_e_quantidade = {}

while viagens != 0:
    qtd_produtos = verificar_produtos()

    for i in range(qtd_produtos):
        registrar_produtos()
    
    qtd_compras = escolher_produtos()
    for i in range(qtd_compras):
        registrar_compras()

    viagens -= 1
    
print(prods_e_preços)
