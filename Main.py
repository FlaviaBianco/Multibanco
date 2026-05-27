from Functions import autenticar_cliente
from Menu import MenuCliente
from Clientes import cliente

while True:

    numero_conta = input("Digite o número da conta: ")
    pin = input("Digite o PIN: ")

    conta = autenticar_cliente(cliente,numero_conta, pin)

    if conta:

        print("\nAutenticação bem-sucedida!")
        print(f"\nBem-vindo, {conta['titular']}!\n")

        print(f"Numero da conta: {numero_conta}\n")

        MenuCliente(conta)

    else:

        print("Número de conta ou PIN incorretos.")
