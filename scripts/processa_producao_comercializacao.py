from utils import download_csv, normalizar_dataframe
import os
import pandas as pd

# Normaliza os dados para torna-los mais legíveis
dicionario_substituicoes = {
    'vm_': 'vinho_mesa_',
    'vv_': 'vinho_viniferas_',
    'su_': '',  # palara 'suco' já existe no cod_produto
    'de_': 'derivados_',
    've_': 'vinho_especial_',
    'es_': '', # palavra 'espumante' já existe no cod_produto
    'ou_': 'outro_',
    '\(': '',
    '\)': '',
    'â': 'a',
    'ç': 'c',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    ' ': '_',
}

def preprocessing(file_path):
    dataframe = pd.read_csv(file_path, sep='[\t;]', engine='python')
    dataframe = normalizar_dataframe(dataframe, dicionario_substituicoes)
    dataframe = dataframe.drop(columns=['id'])
    dataframe.rename(columns={'control': 'cod_produto', 'Produto': 'produto'}, inplace=True)
    dataframe = dataframe.melt(id_vars=['cod_produto', 'produto'], var_name='ano', value_name='litros')
    return dataframe

def main():
    
    directory = 'data'
    items = {
        'producao': 'http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv',
        'comercializacao': 'http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv'
    }
    
    for name, url in items.items():
        filepath = download_csv(url, directory, f'{name}_in.csv')
        dataframe_to_save = preprocessing(filepath)
        
        filepath_output = os.path.join(directory, f'{name}_out.csv')
        dataframe_to_save.to_csv(filepath_output, index=False, sep=';')
        print(f'Dados pré-processados e salvos para {name} em: {filepath_output}')

if __name__ == '__main__':
    main()
