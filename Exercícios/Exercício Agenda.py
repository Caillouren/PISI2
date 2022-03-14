# Agenda com: Cadastros e leitura
agenda = {}
while True:
    print("1 = Cadastro\n2 = Leitura\n3 = Sair")
    opção = int(input("O que você deseja fazer? "))
    if opção == 1:     
        nome = input("Nome:")
        idade = int(input("Idade: "))
        cpf = int(input("Digite o apenas os dígitos do cpf: "))
        agenda[nome] = idade, cpf
        print("Usuário cadastrado!")
    elif opção == 2:
        menores = {}
        for n, i in agenda:
            if i < 18:
                menores[n]
        for n in menores.keys():
            agenda.pop(n)
        print(f"Maiores de idade: {agenda}\n Menores de idade: {menores}")
    elif opção == 3:
        print("Fim do programa")
        break
