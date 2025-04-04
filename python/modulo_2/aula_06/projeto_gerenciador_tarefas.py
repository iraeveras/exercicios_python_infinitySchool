tarefas = []

def inserir_tarefa(nome, descricao, prioridade, categoria, status):
    if nome != "" and descricao != "" and prioridade != "" and categoria != "" and status != "":
        tarefa = {
            "nome": nome,
            "descricao": descricao,
            "prioridade": prioridade,
            "categoria": categoria,
            "status": status,
        }
        tarefas.append(tarefa)

def listar_tarefa():
    for i,item in tarefas:
        print(i, item)

def excluir_tarefa():
    for i in range(len(tarefas)):
        valor = tarefas[i]
        print(i, valor["nome"])

def editar_tarefa():
    print("tarefa editada")

def concluir_tarefa():
    print("tarefa concluida")

def listar_por_prioridade():
    print("lista por prioridade")

def listar_por_categoria():
    print("lista por categoria")

def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefa")
        print("3. Editar tarefa")
        print("4. Excluir tarefa")
        print("5. Marcar tarefa como concluída")
        print("6. Exibir tarefas por prioridade")
        print("7. Exibir tarefas por categoria")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_tarefa()
        elif opcao =="2":
            listar_tarefa()
        elif opcao =="3":
            editar_tarefa()
        elif opcao =="4":
            excluir_tarefa()
        elif opcao =="5":
            concluir_tarefa()
        elif opcao =="6":
            listar_por_prioridade()
        elif opcao =="7":
            listar_por_categoria()
        elif opcao == "8":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida")
