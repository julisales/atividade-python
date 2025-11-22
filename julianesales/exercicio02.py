# lista de tuplas (nome, nota)
dados = [("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9)]

# dicionário para armazenar notas por aluno
alunos = {}

for nome, nota in dados:
    if nome not in alunos:
        alunos[nome] = [nota]      # criando lista de notas
    else:
        alunos[nome].append(nota)  # adicionando nota

# função para pegar a média (pega posição 1 da tupla)
def pegar_media(tupla):
    return tupla[1]

# calculando média de cada aluno
medias = {nome: sum(notas) / len(notas) for nome, notas in alunos.items()}

# ordenando pela média crescente
ordenados = sorted(medias.items(), key=pegar_media)

# exibindo os resultados
for nome, media in ordenados:
    print(f"{nome}: {media:.2f}")