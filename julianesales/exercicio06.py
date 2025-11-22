# importando Counter para contagem de caracteres
from collections import Counter

# função de critério para ordenação
def criterio(item):
    return (-item[1], item[0])

# solicitando frase ao usuário
frase = input("Digite uma frase: ")
# removendo espaços e contando caracteres
frase = frase.replace(" ", "")
contagem = Counter(frase)

# verificando se há pelo menos 3 caracteres únicos
if len(contagem) < 3:
    print("A frase possui menos de 3 caracteres únicos.")
else:
    # transformando o dicionário de contagem em lista de tuplas e ordenando
    ordenados = sorted(contagem.items(), key=criterio)
    # pega o terceiro elemento da lista (índice 2)
    terceiro_caractere, terceira_freq = ordenados[2]
    # exibindo o resultado
    print(f"3º caractere mais frequente: '{terceiro_caractere}'")
    print(f"Quantidade de vezes: {terceira_freq}")