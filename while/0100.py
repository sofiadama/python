numero = int(input('Digite um número entre 1 e 10.000: '))

i = 1
while i <= 10000:
    if i % numero == 2:
        print(i)
    i += 1
