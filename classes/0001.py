class Expoente3:
    def __init__(self, numero):
        self.numero = numero
        self.cubo = self.elevar_ao_cubo()

    def elevar_ao_cubo(self):
        return self.numero**3
    
    def __str__(self):
        return f'CUBO DE {self.numero}: {self.cubo}'

def obter_numero():
    entrada = input('NÚMERO: ').lower()
    if entrada == 'parar':
        return 'parar'
    return int(entrada)

def main():
    while True:
        entrada = obter_numero()
        if entrada == 'parar':
            print('Encerrando o programa...')
            break
            
        potenciaçao = Expoente3(entrada)
        print(potenciaçao)
        print()

if __name__ == '__main__':
    main()
    
