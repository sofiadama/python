class ClientesPetShop:
    def __init__(self, raça, peso, idade, nome_animal, nome_dono, mensalidade):
        self.raça = raça
        self.peso = peso
        self.idade = idade
        self.nome_animal = nome_animal
        self.nome_dono = nome_dono
        self.mensalidade = mensalidade

class ClienteVIP:
    def __init__(self, restriçao, vantagens):
        self.restriçao = restriçao
        self.vantagens = vantagens

    def possui_restriçao(self):
       print('Possui restrição alimentar!')
    
    def calcular_vantagens(self):
        return "20% de desconto em pacote de banho e tosa!"

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
    if verificar == 'SIM':
        return ClienteVIP

def imprimir_cadastros(cadastro):
    print(f'RAÇA: {cadastro.raça}')
    print(f'PESO: {cadastro.peso} kgs')
    print(f'IDADE: {cadastro.idade} anos/meses')
    print(f'NOME DO ANIMAL: {cadastro.nome_animal}')
    print(f'NOME DO DONO: {cadastro.nome_dono}')
    print(f'MENSALIDADE: R$ {cadastro.mensalidade:.2f}')

def continuar_cadastros():
    cadastrar = input('\nContinuar cadastrando? ').upper()
    return cadastrar == 'SIM'

def main():
    while True:
        raça = obter_raça() 
        peso = obter_peso()
        idade = obter_idade()
        nome_animal = obter_nome_animal()
        nome_dono = obter_nome_dono()
        mensalidade = obter_mensalidade()

        verificar_cliente_vip()
        cadastro = ClientesPetShop(raça, peso, idade, nome_animal, nome_dono, mensalidade)
        
        print('\nInformações do cliente\n')
        imprimir_cadastros(cadastro)
        
        if not continuar_cadastros():
            break

if __name__ == '__main__':
    main()    
