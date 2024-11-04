trips = int(input('Número de viagens ao mercado: '))
prod_e_preços = {'mamão': 2.19, 'cebola': 3.10, 'tomate': 2.80, 'uva': 2.73,
                 'morango': 6.70, 'repolho': 1.12, 'brocolis': 1.71}

valor_total = []

def produtos():
    for _ in range(trips):
        qtd_produtos = int(input('Quantidade de produtos: '))
        lista_produtos = input('Insira os produtos que deseja comprar (separados por espaço): ').lower().split()
        
        for produto in lista_produtos:
            if produto in prod_e_preços:
                valor_total.append(prod_e_preços[produto])

produtos()
print(f'Valor total: {sum(valor_total)}')
