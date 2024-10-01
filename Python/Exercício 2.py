import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

class ProcessarDados:
    def __init__(self, url):
        self.url = url
        self.df = None
        self.df_limpo = None
        
    def carregar_dados(self):
        self.df = pd.read_csv(self.url, delimiter=',')
        self.df.to_csv('base_bruta_covid_usa.csv', sep=';', index=False)
        
    def mostrar_dados(self):
        print(self.df)
        print(self.df.shape)
        print(self.df.info())
        print(self.df.head())
        
    def limpar_dados(self):
        self.df_limpo = self.df.dropna()
        self.df_limpo = self.df_limpo.drop_duplicates()
        self.df_limpo['date'] = pd.to_datetime(self.df_limpo['date'])
        print('Dados Limpos: Valores nulos removidos e duplicatas excluídas.')
        
    def agrupar_por_colunas(self, colunas, agregados):
        return self.df_limpo.groupby(colunas)[agregados].sum().reset_index()
    
    def calcular_taxa_crescimento(self, df, coluna):
        df = df.copy()
        df['taxa_crescimento'] = df[coluna].pct_change() * 100
        return df
    
    def projetar_tendencias(self, df, coluna, periodo=30):
        df = df[['date', coluna]].dropna()
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date')
        
        df['data_ordinal'] = df['date'].map(pd.Timestamp.toordinal)
                
        x = df['data_ordinal'].values.reshape(-1, 1)
        y = df[coluna].values
        
        modelo = LinearRegression()
        modelo.fit(x, y)
        
        ultima_data = df['data_ordinal'].max()
        dias_futuros = np.arange(ultima_data + 1, ultima_data + periodo + 1).reshape(-1, 1)
        previsao = modelo.predict(dias_futuros)
        
        dias_futuros_datas = [pd.Timestamp.fromordinal(int(d)) for d in dias_futuros.flatten()]
        
        plt.figure(figsize=(10, 6))
        plt.plot(df['date'], df[coluna], label=f'Casos reais ({coluna})', color='blue')
        plt.plot(dias_futuros_datas, previsao, label='Previsão Futura', linestyle='--', color='red')
        plt.title(f'Projeção de {coluna.capitalize()} para os próximos {dias_futuros} dias')
        plt.xlabel('Data')
        plt.ylabel(coluna.capitalize())
        plt.legend()
        plt.grid(True)
        plt.show(block=True)
    
    def salvar_dados(self, df, nome_arquivo):
        df.to_csv(nome_arquivo, sep=';', index=False)
        

class VisualizadorDados:
    def plot_top_estados(self, df, column, top_n=10, title=""):
        top_estados = df.sort_values(by=column, ascending=False).head(top_n)
        top_estados.plot(kind='bar', x='state', y=column, color='skyblue', legend=False)
        plt.title(title)
        plt.xlabel('Estado')
        plt.ylabel(column.capitalize())
        plt.xticks(rotation=45)
        plt.show(block=True)
        
    def plot_comparar_estados(self, df, estados, title):
        df_filtrado = df[df['state'].isin(estados)]
        df_filtrado = df_filtrado.sort_values(by='date')
        
        df_grupo = df_filtrado.groupby(['date', 'state'])['cases'].sum().unstack().fillna(0)
        
        df_grupo.plot(figsize=(10, 6), title=title)
        plt.xlabel('Data')
        plt.ylabel('Casos')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show(block=True)
        
    def plot_correlacao(self, df, state):
        df_filtrado = df[df['state'] == state]
        plt.scatter(df_filtrado['cases'], df_filtrado['deaths'], alpha=0.5)
        plt.title(f'Correlação entre Casos e Mortes - {state}')
        plt.xlabel('Casos')
        plt.ylabel('Mortes')
        plt.grid(True)
        plt.show(block=True)
        
        
def main():
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
    processo = ProcessarDados(url)
    
    processo.carregar_dados()
    # processor.mostrar_dados()
    processo.limpar_dados()
    
    total_por_estado = processo.agrupar_por_colunas(['state'], ['cases', 'deaths'])
    total_por_fips = processo.agrupar_por_colunas(['fips'], ['cases', 'deaths'])
    total_por_dia = processo.agrupar_por_colunas(['date'], ['cases', 'deaths'])
    
    visualizar = VisualizadorDados()
    # visualizar.plot_top_estados(total_por_estado, 'cases', 10, 'Top 10 Estados com mais casos')
    # visualizar.plot_top_estados(total_por_estado, 'deaths', 10, 'Top 10 Estados com mais mortes')
    
    # visualizar.plot_comparar_estados(processo.df_limpo, ['New York', 'California', 'Florida'], "Comparação de Casos entre Estados")
    
    # visualizar.plot_correlacao(processo.df_limpo, 'New York')
    
    df_ny =processo.df_limpo[processo.df_limpo['state'] == 'New York']
    
    # df_ny_taxa = processo.calcular_taxa_crescimento(df_ny, 'cases')
    # print(df_ny_taxa[['date', 'cases', 'taxa_crescimento']].tail())
    
    processo.projetar_tendencias(df_ny, 'cases', 330)
    
    casos_ny_tempo = df_ny.groupby('date')[['cases', 'deaths']].sum().reset_index()
    
    processo.salvar_dados(casos_ny_tempo, 'casos_ny_tempo.csv')
    
if __name__ == '__main__':
    main()