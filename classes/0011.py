class Funcionário:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_15(self):
        self.salario += self.salario*0.15
        return self.salario
        
    def aumentar_10(self):
        self.salario += self.salario*0.10
        return self.salario

    def aumentar_5(self):
        self.salario += self.salario*0.05
        return self.salario
            
def obter_funcionario():
    return input('FUNCIONÁRIO: ').title()

def obter_salario():
    while True:
        try:
            return float(input('SALÁRIO ATUAL: R$ '))
        except ValueError:
            print('Valor inválido, digite novamente.')
            print()

def deseja_continuar():
    continuar = input('Deseja continuar checando? ').capitalize()
    return continuar == 'Sim'

def controle_do_Funcionário():
    while True:
        for i in range(3):
            print(f'{i+1}º REGISTRO:')
            print()
            nome = obter_funcionario()
            salario = obter_salario()

            atualizaçao = Funcionário(nome, salario)

            if salario <= 2000:
                print(f'NOVO SALÁRIO: R$ {atualizaçao.aumentar_15():.2f}')
            
            elif salario > 2000 and salario <= 3000:
                print(f'NOVO SALÁRIO: R$ {atualizaçao.aumentar_10():.2f}')

            elif salario > 3000:
                print(f'NOVO SALÁRIO: R$ {atualizaçao.aumentar_5():.2f}')
            print()

        if not deseja_continuar():
            break
        print()

if __name__ == '__main__':
    controle_do_Funcionário()
