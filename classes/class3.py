class Salario:
    def __init__(self, nome, salario, aumento):
        self.nome = nome
        self.salario = salario

    def aumentar_15(self):
        if self.salario <= 2000:
            aumento = self.salario*0.15
            self.salario += aumento
            return self.salario
        
    def aumentar_10(self):
        if self.salario > 2000 and self.salario <= 3000:
            aumento = self.salario*0.10
            self.salario += aumento
            return self.salario

    def aumentar_5(self):
        if self.salario > 3000:
            aumento = self.salario*0.05
            self.salario += aumento
            return self.salario

def obter_funcionario():
    return input('NOME: ')

def obter_salario():
    return float(input('SALÁRIO: '))

def main():
    while True:
        nome = obter_funcionario()
        salario = obter_salario()

        funcionario = Salario(nome, salario)

if __name__ == '__main__':
    main()
