def MenuCliente (cliente):

    while True:

        print("1. Consultar saldo")
        print("2. Realizar Levantamento")
        print("3. Realizar Depósito")
        print("4. Realizar Transferência")
        print("5. Consultar Movimentos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            
            case "1":
                print(f"Saldo atual: €{cliente['saldo']}")

            case "2":
                print(f"Saldo: €{cliente['saldo']}")
                Levantar(cliente)

            case "3":
                print(f"Saldo: €{cliente['saldo']}")

            case "4":
                print(f"Saldo: €{cliente['saldo']}")

            case "5":
                print(f"Movimentos: {cliente['movimentos']}")

            case "6":
                break

            case default:
                print("Opção inválida")