import Clientes

def autenticar_cliente(clientes, numero_conta, pin_introduzido):

    if numero_conta not in clientes:
        print("Conta não encontrada!")
        return None

    conta = clientes[numero_conta]

    try:
        if conta["bloqueado"] == True:
            print("Conta bloqueada! Contacte o banco.")
            return False
    except KeyError:
        conta["bloqueado"] = False

    try:
        if pin_introduzido == conta["pin"]:
            conta["tentativas"] = 0
            return conta
        
        else:
            conta["tentativas"] = conta["tentativas"] + 1
            tentativas_restantes = 3 - conta["tentativas"]
            
            if tentativas_restantes > 0:
                print(f"PIN incorreto! Tentativas restantes: {tentativas_restantes}")
                return None
            
            else:
                conta["bloqueado"] = True
                print("Conta bloqueada por excesso de tentativas!")
                return False

    except KeyError:
        conta["tentativas"] = 0
        print("Dados da conta incompletos, tente novamente.")
        return False
    

""" 
import Clientes

def autenticar_cliente(clientes, numero_conta, pin_introduzido):
    
    for c in clientes:

        if c == numero_conta:
            
            conta = clientes[c]

            if conta["bloqueado"] == True:

                print("Conta bloqueada! Contacte o banco.")

                return False
            
            else:
                if pin_introduzido == conta["pin"]:
                    conta["tentativas"] = 0
                    return conta
                
                else:
                    conta["tentativas"] += 1
                    tentativas_restantes = 3 - conta["tentativas"]
                    
                    if tentativas_restantes > 0:

                        print(f"PIN incorreto! Tentativas restantes: {tentativas_restantes}")

                        return None
                    
                    else:

                        conta["bloqueado"] = True

                        print("Conta bloqueada por excesso de tentativas!")

                        return False
       
        
else:
    print("Conta não encontrada!")
    return None
    
"""

def tranferencia(clientes, origem, destino, valor):

    if origem in clientes and destino in clientes:

        if clientes[origem]["saldo"] >= valor:

            clientes[origem]["saldo"] -= valor
            clientes[destino]["saldo"] += valor

            print("Transferência realizada!")

        else:
            print("Saldo insuficiente!")

    else:
        print("Conta não encontrada!")