import random

numero = int(input('Adivinhe o número de 0 a 10: '))
resposta = random.randint(0,10)
tentativas = 0

while numero != resposta:
    numero = int(input('Resposta errada, tente novamente: '))
    tentativas +=1

else:
    tentativas += 1
    print()
    print(f'Parabéns! {resposta} é o número correto!')
    print(f'Tentativas: {tentativas}')
