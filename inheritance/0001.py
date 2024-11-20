class ClientesPetShop:
    def __init__(self, raça, peso, idade, nome_animal, nome_dono, mensalidade):
        self.raça = raça
        self.peso = peso
        self.idade = idade
        self.nome_animal = nome_animal
        self.nome_dono = nome_dono
        self.mensalidade = mensalidade

def obter_raça():
    return input('Raça: ')
    
def obter_peso():
    while True:
        try:
            return float(input('Peso: '))
        except ValueError:
            print('Valor inválido.')
    
def obter_idade():
    while True:
        try:
            return float(input('Idade: '))
        except ValueError:
            print('Valor inválido.')
    
def obter_nome_animal():
    return input('Nome do animal: ').title()
    
def obter_nome_dono():
    return input('Nome do dono: ').title()
    
def obter_mensalidade():
    return float(input('Mensalidade: '))

def verificar_cliente_vip():
    verificar = input('Possui convênio VIP? ').upper()
    return verificar == 'SIM'

def imprimir_cadastros(cadastro):
    print(f'RAÇA: {cadastro.raça}')
    print(f'PESO: {cadastro.peso} kgs')
    print(f'IDADE: {cadastro.idade} anos/meses')
    print(f'NOME DO ANIMAL: {cadastro.nome_animal}')
    print(f'NOME DO DONO: {cadastro.nome_dono}')
    print(f'MENSALIDADE: R$ {cadastro.mensalidade:.2f}')

class ClienteVIP:
    def __init__(self, restricao, vantagens):
        self.restricao = restricao
        self.vantagens = vantagens

    def possui_restricao(self):
        print('Possui restrição alimentar!')
    
    def obter_banhos():
        try:
            banhos = int(input('Banhos por mês: '))
            return banhos
        except ValueError:
            print('Valor inválido.')
            return 0
    
    def calcular_vantagens(self, banhos):
        self.vantagens = banhos * 25

    def __str__(self):
        return f"A mensalidade é de R$ {self.vantagens:.2f}"

def imprimir_VIP(extras):
    print(f'Restrição alimentar: {extras.restricao}')
    print(extras)

def continuar_cadastros():
    cadastrar = input('\nContinuar cadastrando?\n').upper()
    return cadastrar == 'SIM'

def main():
    while True:
        raça = obter_raça() 
        peso = obter_peso()
        idade = obter_idade()
        nome_animal = obter_nome_animal()
        nome_dono = obter_nome_dono()
        mensalidade = obter_mensalidade()
        
        cadastro = ClientesPetShop(raça, peso, idade, nome_animal, nome_dono, mensalidade)
        
        if verificar_cliente_vip():
            
            banhos = extras.obter_banhos()

            extras.calcular_vantagens(banhos)
            extras = ClienteVIP(restricao, vantagens)

        print('\nInformações do cliente\n')
        imprimir_cadastros(cadastro)
        imprimir_VIP()
        
        if not continuar_cadastros():
            break

if __name__ == '__main__':
    main()    
