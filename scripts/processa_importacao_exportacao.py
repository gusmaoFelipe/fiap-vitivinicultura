from utils import download_csv, normalizar_dataframe
import os
import pandas as pd

# Normaliza os dados para torna-los mais legíveis
dicionario_substituicoes = {
    '\(':'_',
    '\"':'',
    '\)': '',
    'à':'a',
    'á':'a',
    'â':'a',
    'ç':'c',
    'é':'e',
    'í':'i',
    'ó':'o',
    'ú':'u',
    'ã':'a',
    'õ':'o',
    'ô':'o',
    '\*':'',
    'nd':''
}

def preprocessing(file_path):
    dataframe = pd.read_csv(file_path, sep='[\t;]', engine='python')
    dataframe = normalizar_dataframe(dataframe, dicionario_substituicoes)
    dataframe.rename(columns={'país': 'pais'}, inplace=True)

    # Separa colunas
    dataframe_kilo_anos = dataframe.iloc[:, 2::2] # anos com valores de kilo 
    dataframe_valor_anos = dataframe.iloc[:, 3::2] # anos com valores financeiros
    dataframe_paises = dataframe.iloc[:, 1:2] # países

    # Junta colunas de países com valores de anos 
    dataframe_kilo_pais = dataframe_paises.join(dataframe_kilo_anos) # kilo
    dataframe_valor_pais = dataframe_paises.join(dataframe_valor_anos) # valor

    # Pivota tabelas
    dataframe_melted_kilo = dataframe_kilo_pais.melt(id_vars='pais', var_name='ano', value_name='quantidade_kg')
    dataframe_melted_valor = dataframe_valor_pais.melt(id_vars='pais', var_name='ano', value_name='quantidade_valor')

    # Transforma valores de ano para inteiro
    dataframe_melted_valor['ano'] = dataframe_melted_valor['ano'].str[:4].astype('int32')
    dataframe_melted_kilo['ano'] = dataframe_melted_kilo['ano'].str[:4].astype('int32')

    # Junta as duas tabelas
    dataframe = dataframe_melted_valor.merge(dataframe_melted_kilo)

    return dataframe

def main():
    
    directory = 'data'
    importacao = {
        'importacao_vinhos_de_mesa': 'http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv',
        'importacao_espumantes': 'http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv',
        'importacao_uvas_frescas': 'http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv',
        'importacao_uvas_passas': 'http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv',
        'importacao_suco_de_uva': 'http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv'    
    }
    exportacao = {
        'exportacao_vinhos_de_mesa': 'http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv',
        'exportacao_espumantes': 'http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv',
        'exportacao_uvas_frescas': 'http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv',
        'exportacao_suco_de_uva': 'http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv'
    }
    
    # processando arquivos de importação
    importacao_dataframe = pd.DataFrame([])
    for name, url in importacao.items():
        filepath = download_csv(url, directory, f'{name}_in.csv')
        dataframe = preprocessing(filepath)
        dataframe['tipo'] = name
        importacao_dataframe = pd.concat([importacao_dataframe, dataframe], ignore_index=True)
        
    filepath_output = os.path.join(directory, 'importacao_out.csv')
    importacao_dataframe.to_csv(filepath_output, index=False, sep=';')
    print(f'Dados pré-processados e salvos para importacao em: {filepath_output}')
   
    # processando arquivos de exportação
    exportacao_dataframe = pd.DataFrame([])
    for name, url in exportacao.items():
        filepath = download_csv(url, directory, f'{name}_in.csv')
        dataframe = preprocessing(filepath)
        dataframe['tipo'] = name
        exportacao_dataframe = pd.concat([exportacao_dataframe, dataframe], ignore_index=True)
        
    filepath_output = os.path.join(directory, 'exportacao_out.csv')
    exportacao_dataframe.to_csv(filepath_output, index=False, sep=';')
    print(f'Dados pré-processados e salvos para exportacao em: {filepath_output}')

if __name__ == '__main__':
    main()
