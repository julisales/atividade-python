# dicionário com categorias de produtos e preços
produtos = {
    "Alimentação": [12.50, 8.99, 15.30],
    "Limpeza": [5.20, 7.80],
    "Higiene": [10.00, 12.00, 9.50, 14.00]
}

# variáveis para armazenar a maior média e a categoria 
maior_media = 0
categoria_vencedora = ""

# calculando a média de preços por categoria
for categoria, precos in produtos.items():
    media = sum(precos) / len(precos)
    # verificando se é a maior média
    if media > maior_media:
        maior_media = media
        categoria_vencedora = categoria
    
# exibindo a categoria com maior média de preços   
print(f"Categoria com maior média de preços: {categoria_vencedora} ({maior_media:.2f})")