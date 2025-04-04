# Dicionário global para armazenar as tarefas
tarefas = {}

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade da tarefa (alta, média, baixa): ")
    categoria = input("Digite a categoria da tarefa: ")
    
    # Criando a tarefa como um dicionário
    tarefa = {
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    
    # Adicionando a tarefa ao dicionário global
    tarefas[nome] = tarefa
    print(f"Tarefa '{nome}' adicionada com sucesso!")

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    for nome, info in tarefas.items():
        status = "Concluída" if info["concluida"] else "Pendente"
        print(f"\nNome: {nome}")
        print(f"Descrição: {info['descricao']}")
        print(f"Prioridade: {info['prioridade']}")
        print(f"Categoria: {info['categoria']}")
        print(f"Status: {status}")

# Função para editar uma tarefa
def editar_tarefa():
    nome = input("Digite o nome da tarefa a ser editada: ")
    
    if nome in tarefas:
        descricao = input("Digite a nova descrição: ")
        prioridade = input("Digite a nova prioridade (alta, média, baixa): ")
        categoria = input("Digite a nova categoria: ")
        
        tarefas[nome]["descricao"] = descricao
        tarefas[nome]["prioridade"] = prioridade
        tarefas[nome]["categoria"] = categoria
        
        print(f"Tarefa '{nome}' atualizada com sucesso!")
    else:
        print("Tarefa não encontrada.")

# Função para excluir uma tarefa
def excluir_tarefa():
    nome = input("Digite o nome da tarefa a ser excluída: ")
    
    if nome in tarefas:
        del tarefas[nome]
        print(f"Tarefa '{nome}' excluída com sucesso!")
    else:
        print("Tarefa não encontrada.")

# Função para marcar uma tarefa como concluída
def concluir_tarefa():
    nome = input("Digite o nome da tarefa a ser concluída: ")
    
    if nome in tarefas:
        tarefas[nome]["concluida"] = True
        print(f"Tarefa '{nome}' marcada como concluída!")
    else:
        print("Tarefa não encontrada.")

# Função para exibir tarefas por prioridade
def exibir_por_prioridade():
    prioridade = input("Digite a prioridade (alta, média, baixa) para filtrar: ")
    
    tarefas_filtradas = {nome: info for nome, info in tarefas.items() if info["prioridade"] == prioridade}
    
    if tarefas_filtradas:
        for nome, info in tarefas_filtradas.items():
            status = "Concluída" if info["concluida"] else "Pendente"
            print(f"\nNome: {nome}")
            print(f"Descrição: {info['descricao']}")
            print(f"Categoria: {info['categoria']}")
            print(f"Status: {status}")
    else:
        print("Nenhuma tarefa encontrada com essa prioridade.")

# Função para exibir tarefas por categoria
def exibir_por_categoria():
    categoria = input("Digite a categoria para filtrar: ")
    
    tarefas_filtradas = {nome: info for nome, info in tarefas.items() if info["categoria"] == categoria}
    
    if tarefas_filtradas:
        for nome, info in tarefas_filtradas.items():
            status = "Concluída" if info["concluida"] else "Pendente"
            print(f"\nNome: {nome}")
            print(f"Descrição: {info['descricao']}")
            print(f"Prioridade: {info['prioridade']}")
            print(f"Status: {status}")
    else:
        print("Nenhuma tarefa encontrada com essa categoria.")

# Função principal do menu
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Editar tarefa")
        print("4. Excluir tarefa")
        print("5. Marcar tarefa como concluída")
        print("6. Exibir tarefas por prioridade")
        print("7. Exibir tarefas por categoria")
        print("8. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            editar_tarefa()
        elif opcao == "4":
            excluir_tarefa()
        elif opcao == "5":
            concluir_tarefa()
        elif opcao == "6":
            exibir_por_prioridade()
        elif opcao == "7":
            exibir_por_categoria()
        elif opcao == "8":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciando o programa
menu()