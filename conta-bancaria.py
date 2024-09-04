menu = f"""

======= PY BANK =======

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Informe a operação que desejas realizar: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao_escolhida = int(input(menu))

    if opcao_escolhida == 1:

        depositar = float(input("Informe o valor para depósito: "))

        if depositar > 0:
            saldo += depositar
            extrato += f"Depósito no valor de: R${depositar:.2f}\n"

        else:
            print("Operação falhou! Informe um valor acima de 0!")

    elif opcao_escolhida == 2:

        sacar = float(input("Informe o valor do saque: "))

        excedeu_saldo = sacar > saldo
        excedeu_limite = sacar > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        valor_saque = sacar <= 0

        if excedeu_saldo:
            print("Saldo insuficiente!")
        
        elif excedeu_limite:
            print("Operação falhou! O valor máximo de saque permitido é de R$500,00.")
        
        elif excedeu_saques:
            print("Operação falhou! Você excedeu o número de saques!")

        elif valor_saque:
            print("Operação falhou! Insira um valor acima de 0!")

        else:
            saldo -= sacar
            extrato += f"Saque no valor de: R${sacar:.2f}\n"
            numero_saques += 1


    elif opcao_escolhida == 3:
        print("\n========== EXTRATO ==========")
        print("Não foram feitas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")
    
    elif opcao_escolhida == 4:
        print("Encerrando...")
        break

    else:
        print("Essa opção é inválida! Digite novamente a opção desejada!")