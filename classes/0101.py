class NumBinario:
    def __init__(self, numero):
        self.numero = numero
        self.num = []
        
    def dec2bin(self):
        if self.numero == 0:
            self.num == [0]
            return
        
        while self.numero > 0:
            resto = self.numero % 2
            self.num.append(resto)
            self.numero = self.numero // 2
        
        self.inverter_bits()
    
    def inverter_bits(self):
        self.num.reverse()
    
    def __str__(self):
        return f"NÚMERO BINÁRIO: {''.join(map(str, self.num)).zfill(8)}"

def obter_decimal():
    return int(input(f'\nNÚMERO DECIMAL: '))
    
class NumDecimal:
    def __init__(self, numero):
        self.numero = numero
        self.num = 0

    def bin2dec(self):
        bits = [int(bit) for bit in self.numero]
        for pos, bit in enumerate(reversed(bits)):
            if bit == 1:
                peso = 2**(pos)
                self.num += peso

        if not self.validar_binario():
            raise ValueError('Valor inválido.')
        
    def validar_binario(self):
        return all(bit in '01' for bit in self.numero)
    
    def __str__(self):
        return f"NÚMERO DECIMAL: {self.num}"
    
def obter_binario():
    return input(f'\nNÚMERO BINÁRIO: ') 

def main():
    while True:
        try:
            escolha = int(input('\n(1) DECIMAL PARA BINÁRIO \n(2) BINÁRIO PARA DECIMAL \n '))         
        
            if escolha == 1:
                numero = obter_decimal()
                            
                converter = NumBinario(numero)
                converter.dec2bin()
                            
                print(converter)
                
            elif escolha == 2:
                numero = obter_binario()
                
                converter = NumDecimal(numero)
                converter.bin2dec()
                
                print(converter)

        except ValueError:
            print('Valor inválido.')

if __name__ == '__main__':
    main()
