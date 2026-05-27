import Clientes

def autenticar_cliente(clientes, numero_conta, pin_introduzido):
    
    for c in clientes:

        if c == numero_conta:
            
            conta = clientes[c]

            if conta["bloqueado"]:
                print("Conta bloqueada! Contacte o banco.")
                return None

            for tentativa in range(3):
                if pin_introduzido == conta["pin"]:
                    return conta
                else:
                    restantes = 2 - tentativa
                    if restantes > 0:
                        print(f"PIN incorreto! Tentativas restantes: {restantes}")
                        pin_introduzido = input("Introduza o PIN: ")

            conta["bloqueado"] = True
            print("Conta bloqueada por excesso de tentativas!")
            return None

    print("Conta não encontrada!")
    return None


    