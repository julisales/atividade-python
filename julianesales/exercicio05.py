# solicitando ao usuário que digite um número
numero_digitado = input("Digite um número: ")

# se o valor digitado for um número válido
try:
    # convertendo para float
    numero = float(numero_digitado)

    # verificando se é inteiro ou decimal
    if numero.is_integer(): 
        # convertendo para inteiro 
        inteiro = int(numero)

        # exibindo resultados
        print("O número é inteiro.")
        if inteiro % 2 == 0:
            print(f"O número {inteiro} é par.")
        else:
            print(f"O número {inteiro} é ímpar.")

    # se for decimal
    else:
        # separando parte inteira e decimal
        parte_inteira = int(numero)
        parte_decimal = numero - parte_inteira

        # exibindo resultados
        print("O número é decimal.")
        print(f"Parte inteira: {parte_inteira}")
        print(f"Parte decimal: {parte_decimal:.2f}")

# tratando erro de valor inválido
except ValueError:
    print("Erro: valor digitado inválido.")