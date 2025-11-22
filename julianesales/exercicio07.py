# lista de livros com título, ano e preço
livros = [
    {"titulo": "A", "ano": 2020, "preco": 45},
    {"titulo": "B", "ano": 2024, "preco": 80},
    {"titulo": "C", "ano": 2020, "preco": 50},
    {"titulo": "D", "ano": 2022, "preco": 40}
]

# dicionário para agrupar livros por ano
agrupados = {}

# agrupando livros por ano
for livro in livros:
    ano = livro["ano"]
    preco = livro["preco"]
    titulo = livro["titulo"]

    # inicializando ano no dicionário se necessário
    if ano not in agrupados:
        agrupados[ano] = {"titulos": [], "precos": []}

    # adicionando título e preço ao ano correspondente
    agrupados[ano]["titulos"].append(titulo)
    agrupados[ano]["precos"].append(preco)

# exibindo os resultados
for ano in sorted(agrupados.keys()):
    titulos = agrupados[ano]["titulos"]
    precos = agrupados[ano]["precos"]
    media = sum(precos) / len(precos)

    print(f"Ano: {ano}")
    print("Livros:", ", ".join(titulos))
    print(f"Preço médio: R$ {media:.2f}")
    print()