from Clientes import cliente

# Credenciais do administrador
ADMIN_USER = "admin"
ADMIN_PIN  = "0000"


def autenticar_admin():

    """Autentica o administrador. Devolve True se as credenciais estiverem corretas."""
    print("\n--- Acesso Administrador ---")
    user = input("Utilizador: ")
    pin  = input("PIN: ")

    if user == ADMIN_USER and pin == ADMIN_PIN:
        print("\nBem-vindo, Administrador!\n")
        return True
    else:
        print("Credenciais inválidas!")
        return False


#Operações:

"""Cria uma nova conta e insere-a no dicionário de clientes."""

def adicionar_conta():
    
    print("\n--- Adicionar Conta ---")

    numero = input("Número da conta: ").strip()

    if numero in cliente:
        print(f"Erro: a conta '{numero}' já existe.")
        return

    titular = input("Nome do titular: ").strip()
    pin     = input("PIN (4 dígitos): ").strip()
    iban    = input("IBAN: ").strip()

    try:
        saldo = float(input("Saldo inicial (€): "))
    except ValueError:
        print("Valor inválido. A conta não foi criada.")
        return

    cliente[numero] = {
        "titular"   : titular,
        "pin"       : pin,
        "saldo"     : saldo,
        "bloqueado" : False,
        "iban"      : iban,
        "tentativas": 0,
        "movimentos": []
    }

    print(f"\nConta '{numero}' criada com sucesso para '{titular}'.")


def listar_contas():
    """Mostra um resumo de todas as contas existentes."""
    print("\n--- Lista de Contas ---")

    if not cliente:
        print("Nenhuma conta registada.")
        return

    print(f"{'Nº Conta':<10} {'Titular':<20} {'IBAN':<25} {'Saldo':>10} {'Estado'}")
    print("-" * 75)

    for numero, dados in cliente.items():
        estado = "Bloqueada" if dados.get("bloqueado") else "Ativa"
        iban   = dados.get("iban", "N/A")
        print(f"{numero:<10} {dados['titular']:<20} {iban:<25} €{dados['saldo']:>9.2f} {estado}")

    print(f"\nTotal de contas: {len(cliente)}")


def apagar_conta():
    
    print("\n--- Apagar Conta ---")

    numero = input("Número da conta a apagar: ").strip()

    if numero not in cliente:

        print(f"Erro: a conta '{numero}' não existe.")
        return

    titular = cliente[numero]["titular"]

    confirmacao = input(f"Tem a certeza que quer apagar a conta de '{titular}'? (s/n): ").strip().lower()

    if confirmacao == "s":
        del cliente[numero]
        print(f"Conta '{numero}' apagada com sucesso.")
    else:
        print("Operação cancelada.")


def MenuAdmin():

    if not autenticar_admin():
        return

    while True:
        print("1. Adicionar conta")
        print("2. Listar contas")
        print("3. Apagar conta")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                adicionar_conta()
            case "2":
                listar_contas()
            case "3":
                apagar_conta()
            case "4":
                print("Sair menu de adm...\n")
                break
            case _:
                print("Opção inválida.")