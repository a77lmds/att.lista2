alunos = []
while True:
    print("1 - Inserir")
    print("2 - Consultar")
    print("3 - Remover")
    print("4 - Consultar lista completa")
    print("5 - Sair")
    op = input("\nEscolha uma opção: ")

    if op == "1":
        nome == input("Nome do aluno: ")
        alunos.append(nome)
    
    elif op =="2":
        nome = input("Digite o nome para consutar: ")
        if nome in alunos:
            print(f"o aluno {nome} está na lista")
        else:
            print("aluno não encontrado")
        
    elif op == "3":
        nome = input("Nome para remover: ")
        if nome in alunos:
            alunos.remove(nome)
        else:
            print("aluno não encontrado")

    elif op == "4":
        print("lista de alunos:", alunos)

    elif op == "5":
        print("Você saiu")
        break
    else:
        print("opção invalida!")

    
    