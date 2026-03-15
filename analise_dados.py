import pandas as pd

# carregar os dados
dados = pd.read_csv("../dados/empreendedorismo_sc.csv")

print("Primeiras linhas do dataset:")
print(dados.head())

# análise por cidade
empresas_cidade = dados.groupby("cidade")["empresas"].sum()

print("\nEmpresas por cidade:")
print(empresas_cidade)

# análise por setor
empresas_setor = dados.groupby("setor")["empresas"].sum()

print("\nEmpresas por setor:")
print(empresas_setor)
