# lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 20, 23]

# função para verificar se um número é primo
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# separando números primos e não primos
primos = [num for num in numeros if eh_primo(num)]
nao_primos = [num for num in numeros if not eh_primo(num)]

# exibindo os resultados
print("Números primos:", primos)
print("Números não primos:", nao_primos)