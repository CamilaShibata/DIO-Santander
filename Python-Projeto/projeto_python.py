import pandas as pd

catalogo = pd.read_csv("catalogo_agencia_espacial.csv", sep=";", usecols=["nome", "cidade", "area", "telefone"]) #Realiza a leitura do arquivo csv, filtrando apenas as colunas definidas

print(catalogo.loc[catalogo["cidade"]=="Rio de Janeiro"]) #Filtra o conteúdo da tabela apenas pelos campos que contém a cidade "Rio de Janeiro"

catalogo.to_csv("agencias_espaciais_rj.csv", index=False) #Salva um novo arquivo csv, com as especificações filtradas