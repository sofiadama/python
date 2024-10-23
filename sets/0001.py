modalidade = int(input('Digite '1' para futebol, '2' para natação, '3' para vôlei e '4' para basquete '))

futebol = 0
natacao = 0
volei = 0
basquete = 0

verificar = 'SIM'

while verificar == 'SIM':
    if modalidade == '1':
        futebol += 1
    elif modalidade == '2':
        natacao += 1
    elif modalidade == '3':
        volei += 1
    elif modalidade == '4':
        basquete += 1
        
    verificar = input('Deseja continuar verificando? ').upper()

else:
    
