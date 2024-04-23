# Lista para armazenar os clientes
clientes = []

def cadastrar_cliente():
    print("Cadastro de Cliente")
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    
    # Criar um dicionário para representar o cliente
    cliente = {
        'nome': nome,
        'cpf': cpf,
        'endereco': endereco
    }
    
    # Adicionar o cliente à lista de clientes
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    print("\nLista de Clientes")
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Endereço: {cliente['endereco']}")
        print("-" * 20)

def menu():
    while True:
        print("\nBanco XYZ - Cadastro de Clientes")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
