class Clientes:
    def __init__(self):
        self.clientes = []
        self.matriculas = []
        
    def cadastrar_cliente(self, nome, idade, numero):
        novo_cliente = {'nome': nome, 'idade': idade, 'numero': numero}
        self.clientes.append(novo_cliente)
    
    def matricular_cliente(self, nome, idade, rg, cpf, numero, email):
        matricula = {'nome': nome, 'idade': idade, 'rg': rg, 'cpf': cpf, 'numero': numero, 'email': email}
        self.matriculas.append(matricula)

    def atualizar_dados(self, nome):
        clientes_matriculados = [cliente for cliente in self.matriculas if cliente['nome'].title() == nome.title()]
            
        if not clientes_matriculados:
            print('Nome não registrado.')
            return
        
        if len(clientes_matriculados) > 1:
            print('Há mais de um cliente com esse nome.' )
            cpf = int(input(f"Tente pelo CPF: "))
            
            cliente_selecionado = [cliente for cliente in clientes_matriculados if cliente['cpf'] == cpf]
        
            if not cliente_selecionado:
                print("CPF não encontrado entre os clientes com esse nome.")
                return
            
            cliente_selecionado = cliente_selecionado[0]
            
        else:
            cliente_selecionado = clientes_matriculados[0]
        
        while True:
            mostrar_dados()

            try:
                dado = int(input('\nDigite qual dado quer alterar: '))
                
                if dado == 1:
                    cliente_selecionado['nome'] = input('Nome correto: ')
                elif dado == 2:
                    cliente_selecionado['idade'] = int(input('Idade correta: '))
                elif dado == 3:
                    cliente_selecionado['rg'] = int(input('RG correto: '))
                elif dado == 4:
                    cliente_selecionado['cpf'] = int(input('CPF correto: '))
                elif dado == 5:
                    cliente_selecionado['numero'] = int(input('Número correto: '))
                elif dado == 6:
                    cliente_selecionado['email'] = int(input('E-mail correto: '))
                else:
                    print('Opção inválida!')
                    return
                
            except ValueError:
                print('Por favor, digite um número válido.')

            if not deseja_atualizar():
                break

def exibir_menu():
    print('\nMENU\n')
    print('1. Adicionar potencial cliente')
    print('2. Adicionar potencial cliente indicado')
    print('3. Matricular novo aluno')
    print('4. Excluir aluno')
    print('5. Atualizar dados')
    print('6. Listar alunos')
    print('7. Sair')

def mostrar_dados():
    print('\nDADOS\n')
    print('1. Nome')
    print('2. Idade')
    print('3. RG')
    print('4. CPF')     
    print('5. Número')
    print('6. E-mail')

def deseja_atualizar():
    atualizar = input('Deseja atualizar outra informação? ').strip().capitalize()
    return atualizar == 'Sim'

def processar_menu(clientes):
    while True:
        exibir_menu()
        
        try:
            opcao = int(input('\nDigite a opção escolhida (Nº): '))
            
            if opcao == 1 or opcao == 2:
                nome = input('Nome: ')
                idade = int(input('Idade: '))
                numero = int(input('Telefone: '))

                clientes.cadastrar_cliente(nome, idade, numero)
            
            elif opcao == 3:
                nome = input('Nome: ')
                idade = int(input('Idade: '))
                numero = int(input('Telefone: '))
                email = input('E-mail: ')
                cpf = int(input('CPF: '))
                rg = int(input('RG: '))

                clientes.matricular_cliente(nome, idade, numero, email, cpf, rg)
            
            elif opcao == 4:
                nome = input('Digite o nome do cliente a ser excluído: ')
                clientes.excluir_cliente(nome)
            
            elif opcao == 5:
                nome = input('Digite o nome do cliente a ser atualizado: ')
                clientes.atualizar_dados(nome)

            elif opcao == 6:
                clientes.listar_clientes()
            
            elif opcao == 7:
                print('Desligando...')
                break

            else:
                print('Opção inválida! Tente novamente.')

            print('\nAção concluída com sucesso!')

        except ValueError:
            print('Por favor, digite um número válido.')

def main():
    clientes = Clientes()
    processar_menu(clientes)
    
if __name__ == "__main__":
    main()
