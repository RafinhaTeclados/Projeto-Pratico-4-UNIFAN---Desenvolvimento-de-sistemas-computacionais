# [ID, nome, idade, número, telefone]
clientes = [[1, "Rafael Sodré", 21, "74999991111", "Irecê"],
    [2, "Lucas Carneiro", 20, "74999992222", "Irecê"],
    [3, "Kelvin Lima", 20, "74999993333", "Lapão"],
    [4, "Maria Oliveira", 26, "74999994444", "Irecê"],
    [5, "João Silva", 35, "74999995555", "Central"],
    [6, "Ana Costa", 41, "74999996666", "Xique-Xique"],
    [7, "Pedro Souza", 19, "74999997777", "Irecê"],
    [8, "Carla Ribeiro", 49,  "74999998888", "Lapão"],
    [9, "Marcos Pereira", 23, "74999999999", "América Dourada"],
    [10, "Julia Almeida", 18, "74999990000", "Irecê"]]

# [ID_Solicitacao, ID_Cliente (INTEGRAÇÃO), Produto, Motivo, Status]
produtos = [[101, 1, "Sapatênis Couro T41", "Tamanho Incorreto", "Aguardando Postagem"],
    [102, 2, "Bota Nobuck T42", "Defeito na Costura", "Em Análise"],
    [103, 3, "Sandália Confort T37", "Desistência", "Reembolsado"],
    [104, 4, "Sapato Social Premium T40", "Tamanho Incorreto", "Novo Par Enviado"],
    [105, 5, "Tênis Running Sport T39", "Defeito no Solado", "Em Análise"],
    [106, 6, "Sapatilha Flex T35", "Tamanho Incorreto", "Aguardando Postagem"],
    [107, 1, "Bota Trekking Nobuck T41", "Defeito no Passador", "Substituído"],
    [108, 8, "Scarpin Clássico T36", "Desistência", "Aguardando Triagem"],
    [109, 9, "Chinelo Couro Confort T42", "Tamanho Incorreto", "Novo Par Enviado"],
    [110, 10, "Mocassim Nobuck T38", "Defeito na Palmilha", "Reembolsado"]]


def exibe_menu():
    print("\n=== MENU ===")
    print("1 - Gerenciar clientes")
    print("2 - Gerenciar produtos (pós-venda)")
    print("0 - Sair")




def menu_clientes():
    menu_ativo = True


    while menu_ativo:
        print("\n=== MENU DE CLIENTES ===")
        print("1 - Listar clientes")
        print("2 - Cadastrar cliente")
        print("3 - Excluir cliente")
        print("0 - Voltar")


        opcao = int(input("Escolha: "))

        match (opcao):
            case 1:
                listar_clientes()
            case 2:
                cadastrar_cliente()
            case 3:
                excluir_clientes()
            case 0:
                menu_ativo = False
            case _:
                print("\nOpção inválida!")


def menu_produtos():
    menu_ativo = True
    while menu_ativo:
        print("\n=== MENU DE PÓS-VENDA (PRODUTOS) ===")
        print ("1 - Cadastrar produtos")
        print ("2 - Listar produtos")
        print ("3 - Excluir produtos")
        print ("4 - Alterar Status de produto")
        print ("0 - Sair")
        
        opcao = int(input("Escolha: "))
        
        match (opcao):
            case 1:
                cadastrar_produtos()
            case 2:
                listar_produtos()
            case 3:
                excluir_produtos()
            case 4:
                alterar_status_produto()
            case 0:
                menu_ativo = False
            case _:
                print("Opção inválida!")




def cadastrar_cliente():
    
    while True:
        id_cliente = len(clientes) + 1
        print("\n--- CADASTRO DE NOVO CLIENTE ---")
        print("Digite 0 para voltar")


        nome = input("Digite o nome do cliente: ").strip()
        if nome == "0":
            break
        if nome == "":
            print("\nERRO: O nome do cliente não pode ficar em branco!")
            continue

        idade = input("Digite a idade do cliente: ").strip()
        if idade == "0":
            break
        if not idade.isdigit():
            print("Digite apenas números!")
            continue
        idade = int(idade)
        if idade < 18:
            print("Cliente deve ser maior de 18 anos!")
            continue

        telefone = input("Digite o telefone (com DDD): ").strip()
        cidade = input("Digite a cidade: ").strip()
    
        if cidade == "":
            cidade = "Não informada"

        novo_cliente = [id_cliente, nome, idade, telefone, cidade]
        clientes.append(novo_cliente)
        
        print(f"\nCliente '{nome}' cadastrado com sucesso! (ID gerado: {id_cliente})")
        break




def listar_clientes():
    print("\n=========================================================================")
    print("                            LISTA DE CLIENTES                            ")
    print("=========================================================================")


    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    else:
        for cliente in clientes:
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Idade: {cliente[2]} | Tel: {cliente[3]} | Cidade: {cliente[4]}")



def excluir_clientes():
    listar_clientes()

    if not clientes:
        return

    escolha_id = input("\nDigite o ID do cliente que deseja excluir (0 para voltar): ").strip()

    if escolha_id == "0":
        return

    if not escolha_id.isdigit():
        print("Opção inválida! Digite um número de ID válido.")
        return

    id_para_excluir = int(escolha_id)
    for item_produto in produtos:
        if item_produto[1] == id_para_excluir:
            print("\nERRO CRÍTICO: Este cliente não pode ser excluído!")
            print(f"Motivo: Ele possui a solicitação ID {item_produto[0]} pendente no Pós-Venda.")
            return
        
    cliente_encontrado = None
    indice_para_remover = -1

    for i, cliente in enumerate(clientes):
        if cliente[0] == id_para_excluir:
            cliente_encontrado = cliente
            indice_para_remover = i
            break

    if cliente_encontrado is not None:
        removido = clientes.pop(indice_para_remover)
        print(f"Cliente '{removido[1]}' (ID: {removido[0]}) removido com sucesso!")
    else:
        print("ERRO: Nenhum cliente encontrado com esse ID!")


def cadastrar_produtos():
    print("\n--- CADASTRO DE SOLICITAÇÃO (PÓS-VENDA) ---")
    print("Digite 0 em qualquer campo para voltar ao menu")

    if len(produtos) == 0:
        id_produto = 101
    else:
        id_produto = produtos[len(produtos) - 1][0] + 1

    while True:
        id_cliente_input = input("Digite o ID do cliente dono deste produto: ").strip()
        
        if id_cliente_input == "0":
            return
            
        if not id_cliente_input.isdigit():
            print("\nERRO: Digite apenas números para o ID do cliente!")
            continue
            
        id_cliente_procurado = int(id_cliente_input)
        
        cliente_existe = False
        for cliente in clientes:
            if cliente[0] == id_cliente_procurado:
                cliente_existe = True
                break
                
        if not cliente_existe:
            print("\nERRO: Esse ID de cliente não está cadastrado no sistema! Cadastre o cliente primeiro.")
            continue
        break

    while True:
        descricao = input("Digite o nome/descrição do produto: ").strip()
        if descricao == "0":
            return
        if descricao == "":
            print("\nERRO: A descrição do produto não pode ficar em branco!")
            continue
        break

    while True:
        motivo = input("Digite o motivo da troca/devolução: ").strip()
        if motivo == "0":
            return
        if motivo == "":
            print("\nERRO: O motivo não pode ficar em branco!")
            continue
        break

    status_padrao = "Aguardando Triagem"

    nova_linha_produto = [id_produto, id_cliente_procurado, descricao, motivo, status_padrao]
    produtos.append(nova_linha_produto)

    print(f"\nProduto cadastrado com sucesso! (ID da Solicitação: {id_produto})\n")


def listar_produtos():
    print("\n=========================================================================")
    print("                    RELATÓRIO DE PÓS-VENDA (PRODUTOS)                    ")
    print("=========================================================================")
    
    if not produtos:
        print("Nenhuma solicitação de pós-venda cadastrada.")
        return

    for item in produtos:
        
        print(f"Solicitação: {item[0]} | Cliente ID: {item[1]} | Produto: {item[2]}")
        print(f"   └─ Motivo: {item[3]} | Status Atual: {item[4]}")

def excluir_produtos():
    listar_produtos()

    if not produtos:
        return

    while True:
        escolha_id = input("\nDigite o ID da solicitação que deseja excluir (0 para voltar): ").strip()
        if escolha_id == "0":
            return
        if not escolha_id.isdigit():
            print("Opção inválida! Digite um número de ID válido.")
            continue
        break

    id_para_excluir = int(escolha_id)
    produto_encontrado = None
    indice_para_remover = -1

    for i, produto in enumerate(produtos):
        if produto[0] == id_para_excluir:
            produto_encontrado = produto
            indice_para_remover = i
            break

    if produto_encontrado is not None:
        removido = produtos.pop(indice_para_remover)
        print(f"Solicitação ID {removido[0]} ({removido[2]}) excluída com sucesso!")
    else:
        print("ERRO: Nenhuma solicitação encontrada com esse ID!")

def alterar_status_produto():
    listar_produtos()

    if not produtos:
        return


    while True:
        escolha_id = input("\nDigite o ID da solicitação que deseja alterar o status (0 para voltar): ").strip()
        if escolha_id == "0":
            return
        if not escolha_id.isdigit():
            print("Opção inválida!")
            continue
        break

    id_solicitacao = int(escolha_id)
    produto_encontrado = None

    for item_produto in produtos:
        if item_produto[0] == id_solicitacao:
            produto_encontrado = item_produto
            break

    if produto_encontrado is not None:
        print(f"\nAlterando status do produto: {produto_encontrado[2]}")
        print(f"Status atual: {produto_encontrado[4]}")
        print("\nEscolha o novo status:")
        print("1 - Em Análise")
        print("2 - Aguardando Postagem")
        print("3 - Novo Par Enviado")
        print("4 - Reembolsado")
        
        opcao = int(input("Escolha a opção: "))

        match (opcao):    
            case 1:
                produto_encontrado[4] = "Em Análise"
            case 2:
                produto_encontrado[4] = "Aguardando Postagem"
            case 3:
                produto_encontrado[4] = "Novo Par Enviado"
            case 4:
                produto_encontrado[4] = "Reembolsado"
            case _:
                print("Opção inválida! O status não foi alterado.")
                return

        print(f"Status atualizado com sucesso para: '{produto_encontrado[4]}'")
    else:
        print("ERRO: Nenhuma solicitação encontrada com esse ID!")


while True:
    exibe_menu()
    opcao = int(input("Escolha: "))

    match(opcao):
        case 1:
            menu_clientes()
        case 2:
            menu_produtos()
        case 0:
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida!")
