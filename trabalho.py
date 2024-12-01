class Clientes:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, idade, numero):
        self.clientes.append({'nome': nome, 'idade': idade, 'numero': numero})

    def listar_clientes(self):
        print('\nLista de Clientes:\n')
        for cliente in self.clientes:
            print(cliente)

class Alunos(Clientes):
    def __init__(self):
        super().__init__()
        self.matriculas = []

    def matricular_aluno(self, nome, idade, rg, cpf, numero, email):
        self.matriculas.append({'nome': nome, 'idade': idade, 'rg': rg, 'cpf': cpf, 'numero': numero, 'email': email})

    def buscar_aluno(self, nome):
        for aluno in self.matriculas:
            if aluno['nome'].title() == nome.title():
                return aluno
        print(f'Aluno "{nome}" não encontrado.')
        return None

    def atualizar_dados(self, nome):
        aluno = self.buscar_aluno(nome)
        if not aluno:
            return

        dados = {
            1: ('Nome', str), 2: ('Idade', int), 3: ('RG', int),
            4: ('CPF', int), 5: ('Número', int), 6: ('E-mail', str)
        }
        
        while True:
            print('\nDADOS\n1. Nome\n2. Idade\n3. RG\n4. CPF\n5. Número\n6. E-mail')
            try:
                dado = int(input('\nEscolha o dado a alterar: '))
                if dado not in dados:
                    print('Opção inválida!')
                    return
                info, tipo = dados[dado]
                aluno[info] = tipo(input(f'{info}: '))
            except ValueError:
                print('Valor inválido.')

            if input('Atualizar outro dado? (Sim/Não): ').strip().capitalize() != 'Sim':
                break

    def remover_aluno(self, nome):
        aluno = self.buscar_aluno(nome)
        if aluno:
            self.matriculas.remove(aluno)
            print(f'Aluno "{nome}" removido com sucesso!\n')

    def listar_alunos(self):
        print('\nLista de Alunos:\n')
        for aluno in self.matriculas:
            print(aluno)

class ClientesIndicados(Clientes):
    pass

def mostrar_menu():
    print('\nMENU\n1. Adicionar cliente\n2. Adicionar cliente indicado\n3. Matricular aluno\n4. Atualizar dados\n5. Excluir aluno\n6. Listar clientes\n7. Listar alunos\n8. Sair')

def processar_menu(clientes, alunos, clientes_indicados):
    while True:
        mostrar_menu()
        try:
            opcao = int(input('\nEscolha uma opção: '))
            if opcao == 1:
                nome, idade, numero = input('Nome: ').title(), int(input('Idade: ')), int(input('Telefone: ')) 
                clientes.cadastrar_cliente(nome, idade, numero)
            elif opcao == 2:
                nome, idade, numero = input('Nome: ').title(), int(input('Idade: ')), int(input('Telefone: ')))
                clientes_indicados.cadastrar_cliente(nome, idade, numero)
            elif opcao == 3:
                nome = input('Nome: ').title()
                idade, numero, email, cpf, rg = int(input('Idade: ')), int(input('Telefone: ')), input('E-mail: '), int(input('CPF: ')), int(input('RG: ')) 
                alunos.matricular_aluno(nome, idade, rg, cpf, numero, email)
                print('Aluno matriculado com sucesso!')
            elif opcao == 4:
                nome = input('Nome do aluno: ').title()
                alunos.atualizar_dados(nome)
            elif opcao == 5:
                nome = input('Nome do aluno a remover: ').title()
                alunos.remover_aluno(nome)
            elif opcao == 6:
                clientes.listar_clientes()
            elif opcao == 7:
                alunos.listar_alunos()
            elif opcao == 8:
                print('Saindo...')
                break
            else:
                print('Opção inválida.')
        except ValueError:
            print('Entrada inválida, digite um número.')

def main():
    clientes, alunos, clientes_indicados = Clientes(), Alunos(), ClientesIndicados()
    processar_menu(clientes, alunos, clientes_indicados)

if __name__ == "__main__":
    main()
