from Functions import autenticar_cliente
from Menu import MenuCliente
from MenuAdmin import MenuAdmin
from Clientes import cliente

while True:

    print("1. Acesso Cliente")
    print("2. Acesso Administrador")
    print("0. Sair")    
    print()
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print ()

        numero_conta = input("Digite o número da conta: ")
        pin = input("Digite o PIN: ")

        conta = autenticar_cliente(cliente,numero_conta, pin)

        if conta == False:
            continue

        if conta:

            print("\nAutenticação bem-sucedida!")
            print(f"\nBem-vindo, {conta['titular']}!\n")

            print(f"Numero da conta: {numero_conta}\n")

            MenuCliente(conta, numero_conta)

        else:

            print("Número de conta ou PIN incorretos.")

    elif opcao == "2":
        MenuAdmin()

    elif opcao == "0":
        
        print ("Encerrando, obrigada!")
        break

    else:

        print("Opção inválida.")

        print ("-"*30)


