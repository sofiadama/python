class NumBinario:
    def __init__(self, numero):
        self.numero = numero
        self.num = []
        
    def dec2bin(self):
        if self.numero == 0:
            return self.num == [0]
        
        while self.numero > 0:
            resto = self.numero % 2
            self.num.append(resto)
            self.numero = self.numero // 2
        
        self.inverter_bits()
    
    def inverter_bits(self):
        return self.num.reverse()
    
    def __str__(self):
        return f"NÚMERO BINÁRIO: {''.join(map(str, self.num)).zfill(8)}"

def obter_numero():
    return int(input('NÚMERO DECIMAL: '))


def main():
    while True:
        numero = obter_numero()
        
        converter = NumBinario(numero)
        converter.dec2bin()
        
        print(converter)
        print()
        
if __name__ == '__main__':
    main()
