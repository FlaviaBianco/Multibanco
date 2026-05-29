from Functions import tranferencia
from Clientes import cliente as clientes

def MenuCliente (conta, numero_conta):

    while True:

        print("-" * 30)
        print("1. Consultar saldo")
        print("2. Realizar Levantamento")
        print("3. Realizar Depósito")
        print("4. Realizar Transferência")
        print("5. Consultar Movimentos")
        print("6. Sair")
        print("-" * 30)

        opcao = input("Escolha uma opção: ")

        match opcao:
            
            case "1":

                print ()
                print(f"Saldo atual: €{conta['saldo']}")
                print ("-"*30)
                print()

            case "2":

                print(f"Saldo: €{conta['saldo']}")
                Levantar(conta)

                """(levantamento) Pedir o valor ao utilizador
                Verificar se o valor é válido (maior que 0)
                Verificar se há saldo suficiente
                Subtrair o valor ao saldo da conta
                Mostrar confirmação com o novo saldo"""

                # e também fazer a função no arquivo functions e importar no topo desse arquivo, assim como eu fiz com as transferências

            case "3":

                print(f"Saldo: €{conta['saldo']}")

                """(Depósito) Pedir o valor ao utilizador
                Verificar se o valor é válido (maior que 0)
                Adicionar o valor ao saldo da conta
                Mostrar confirmação com o novo saldo"""

                # e também fazer a função no arquivo functions e importar no topo desse arquivo, assim como eu fiz com as transferências

            case "4":

                print ()
                print(f"Saldo: €{conta['saldo']}")
                iban_destino = input("IBAN de destino: ")
                valor = float(input("Valor a transferir: €"))
                
                conta_destino = None

                for num, dados in clientes.items():
                    if dados["iban"] == iban_destino:
                        conta_destino = num
                        break
                
                if conta_destino:
                    tranferencia(clientes, numero_conta , conta_destino, valor)
                else:
                    print("Conta não encontrada!")

                print ()



            case "5":
                """print(f"Movimentos: {conta['movimentos']}")"""

                print ()

                movimentos = conta['movimentos']
                ultimos10 = movimentos[-10:]
                
                if not ultimos10:
                    print("Não há movimentos registados.")
                else:
                    print("\n--- Últimos Movimentos ---")
                    for m in ultimos10:
                        print(f"Tipo: {m['tipo']} | Valor: €{m['valor']} | Data: {m['data']} | Descrição: {m['descricao']}")
                        

            case "6":
                break

            case default:

                print("Opção inválida")

                print ()