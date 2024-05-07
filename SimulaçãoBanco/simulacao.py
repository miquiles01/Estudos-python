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
    if not clientes:
        print("Não há clientes cadastrados.")
        return
    
    print("\nLista de Clientes")
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Endereço: {cliente['endereco']}")
        print("-" * 20)

def atualizar_cliente():
    if not clientes:
        print("Não há clientes cadastrados para atualizar.")
        return
    
    cpf = input("Digite o CPF do cliente que deseja atualizar: ")
    
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("Dados do cliente encontrado:")
            print(f"Nome: {cliente['nome']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"Endereço: {cliente['endereco']}")
            
            novo_nome = input("Digite o novo nome do cliente (ou enter para manter o mesmo): ")
            novo_endereco = input("Digite o novo endereço do cliente (ou enter para manter o mesmo): ")
            
            if novo_nome:
                cliente['nome'] = novo_nome
            if novo_endereco:
                cliente['endereco'] = novo_endereco
            
            print("Cliente atualizado com sucesso!")
            return
    
    print("Cliente não encontrado.")

def deletar_cliente():
    if not clientes:
        print("Não há clientes cadastrados para deletar.")
        return
    
    cpf = input("Digite o CPF do cliente que deseja deletar: ")
    
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            clientes.remove(cliente)
            print("Cliente deletado com sucesso!")
            return
    
    print("Cliente não encontrado.")

def menu():
    while True:
        print("\nBanco XYZ - Cadastro de Clientes")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Deletar cliente")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            atualizar_cliente()
        elif opcao == '4':
            deletar_cliente()
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
