""" INFORMAÇÕES:
A cada 1000kg = 1 crédito de carbono
1 crédito = US$5,00 dólares
1 hectare de terra compensa 10 toneladas de carbono """

credito = 5
hectare = 10
saldo = 0

def opcao_compra():
    global saldo
    co2 = float(input("Digite a quantidade de CO2 emitido em (Kg): "))
    co2 /= 1000
    valor_dolar = (co2 * credito)
    total_creditos = (valor_dolar / credito)
    saldo += total_creditos
    print('-' * 40)
    print(f"Você pagará US${valor_dolar:.2f} e receberá {total_creditos:.2f} créditos de carbono.")

    confirmacao = input("Confirmar compra ('sim'/'nao'): ")
    if confirmacao.lower() == "sim" or confirmacao.lower() == "s":
        print('-' * 40)
        print(f"Agora você tem {total_creditos:.2f} créditos de carbono.")
    else:
        print('-' * 40)
        print("Compra cancelada.")


def opcao_venda():
    global saldo
    terra = float(input("Quantos hectares de terra plantada você possui?: "))
    total_creditos = ((terra * hectare)/credito)
    print('-' * 40)
    if saldo > 0:
        saldo += total_creditos
        
        print(f"Você tem {saldo:.2f} créditos de carbono ")
        print('-' * 40)

        venda_credito = float(input("Quantos créditos de carbono deseja vender?: "))

        if venda_credito <= saldo:
            print('-' * 40)
            saldo -= venda_credito
            valor_venda = (venda_credito * credito)
            print(f"Você receberá US${valor_venda:.2f} e sobrará {saldo:.2f} créditos de carbono pela venda.")

            confirmacao = input("Confirmar venda ('sim'/'nao')?: ")

            if confirmacao.lower() == "sim" or confirmacao.lower() == "s":
                print('-' * 40)
                print(f"Você recebeu US${valor_venda:.2f} pela venda.")
                print(f"Agora você tem {saldo:.2f} créditos de carbono.")
            else:
                print('-' * 40)
                print("Venda cancelada.")
        
        else:
            print('-' * 40)
            print("Não tem créditos suficientes para a venda.")


    elif saldo <= 0 and total_creditos <= 0:
        print("Não tem créditos suficientes para a venda.")


    else:
        print(f"Você tem {total_creditos:.2f} créditos de carbono ")
        print('-' * 40)
        venda_credito = float(input("Quantos créditos de carbono deseja vender?: "))

        if venda_credito > total_creditos:
            print('-' * 40)
            print("Não tem créditos suficientes para a venda.")

        else:
            total_creditos -= venda_credito
            saldo += total_creditos
            valor_venda = (venda_credito * credito)
            print(f"Você receberá US${valor_venda:.2f} e sobrará {saldo:.2f} créditos de carbono pela venda.")

            confirmacao = input("Confirmar venda ('sim'/'nao')?: ")

            if confirmacao.lower() == "sim" or confirmacao.lower() == "s":
                print('-' * 40)
                print(f"Você recebeu US${valor_venda:.2f} pela venda.")
                print(f"Agora você tem {saldo:.2f} créditos de carbono.")
            else:
                print('-' * 40)
                print("Venda cancelada.")
    

while True:
    print('-' * 40)
    print(""" SELECIONE A OPÇÃO DE NEGÓCIO:
      1 - Comprar créditos
      2 - Vender créditos
      3 - Visualizar saldo
      4 - Sair 
      """)

    opcao = int(input("Digite o número da opção: "))

    if opcao == 1:
        print('-' * 40)
        opcao_compra()
    elif opcao == 2:
        print('-' * 40)
        opcao_venda()
    elif opcao == 3:
        print('-' * 40)
        print(f"Seu saldo é de {saldo:.2f} créditos de carbono.")
    elif opcao == 4:
        print('-' * 40)
        print("Obrigado por usar o sistema de compra e venda. Adeus!")
        break
    else:
        print('-' * 40)
        print("Opção inválida. Tente novamente.")
