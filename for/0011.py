def str(Aluno):
    n = []
for n in range(5):
    nome = input("Aluno:")
    nota = float(input("Nota:"))
    valor_mensal = float(input("Mensalidade:"))
    
    if nota >= 10:
        return("O aluno com a melhor nota é",nome,", o valor de sua mensalidade antes era de R$",valor_mensal,"e agora, com 30% de desconto aplicados é de R$",valor_mensal - valor_mensal*0.30)
