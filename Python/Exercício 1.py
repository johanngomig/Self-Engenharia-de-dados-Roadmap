import pandas as pd

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
df = pd.read_csv(url, delimiter=',')

df.to_csv('base_bruta_covid_usa.csv', sep=';', index=False)

# print(df) # Exibir o DataFrame
# print(df.shape) # Exibir o número de linhas e colunas
# print(df.info()) # Exibir informações do DataFrame, como tipos de dados e valores nulos
# print(df.head()) # Exibir as cinco primeiras linhas do DataFrame

# print(df.isnull().sum()) # Exibir quantos valores nulos existem em cada coluna
df_limpa = df.dropna() # Remover as linhas com valores nulos
# print(df_limpa)

# print(df_limpa.duplicated().sum()) # Exibir quantas linhas duplicadas existem
df_limpa = df_limpa.drop_duplicates() # Remover as linhas duplicadas
# print(df_limpa)

total_por_estado = df_limpa.groupby('state')[['cases', 'deaths']].sum().reset_index()
# print(total_por_estado)

total_por_dia = df_limpa.groupby('date')[['cases', 'deaths']].sum().reset_index()
# print(total_por_dia)

total_por_fips = df_limpa.groupby('fips')[['cases', 'deaths']].sum().reset_index()
# print(total_por_fips)

estados_mais_casos = total_por_estado.sort_values(by='cases', ascending=False).head(10)
# print(estados_mais_casos)

estados_mais_mortes = total_por_estado.sort_values(by='deaths', ascending=False).head(10)
# print(estados_mais_mortes)

df_limpa['date'] = pd.to_datetime(df_limpa['date']) # Converter a coluna 'date' para o formato datetime

new_york_dados = df_limpa[df_limpa['state'] == 'New York'] # Filtrar apenas os dados de New York
casos_ny_tempo = new_york_dados.groupby('date')[['cases', 'deaths']].sum().reset_index() # Agrupar os dados por data e somar os casos
# print(casos_ny_tempo)

casos_ny_tempo.to_csv('casos_ny_tempo.csv', sep=';', index=False)

