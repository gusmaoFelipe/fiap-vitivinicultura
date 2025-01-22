from utils import download_csv, normalizar_dataframe
import os
import pandas as pd

# Normaliza os dados para torna-los mais legíveis
dicionario_substituicoes = {
    'ti_':'tintas_',
    '^sc$':'sem_classificacao',
    ' ':'',
    'outras_[0-9]':'outras',
    'br_':'brancaserosadas_',
    '\(':'_',
    '\"':'',
    '\)': '',
    'à':'a',
    'á':'a',
    'ç':'c',
    'é':'e',
    'í':'i',
    'ó':'o',
    'ú':'u',
    'ã':'a',
    'õ':'o',
    '\*':'',
    'nd':''
}

def preprocessing(file_path):
    dataframe = pd.read_csv(file_path, sep='[\t;]', engine='python')
    dataframe = normalizar_dataframe(dataframe, dicionario_substituicoes)
    dataframe = dataframe.drop(columns=['id', 'cultivar'])
    dataframe = dataframe.melt(id_vars=['control'], var_name='ano', value_name='quantidade_kg')
    return dataframe

def main():
    
    directory = 'data'
    items = {
        'processamento_viniferas': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv',
        'processamento_americanas_e_hibridas': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv',
        'processamento_uvas_de_mesa': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv',
        'processamento_sem_classificacao': 'http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv'
    }
    
    dataframe_to_save = pd.DataFrame([])
    for name, url in items.items():
        filepath = download_csv(url, directory, f'{name}_in.csv')
        dataframe = preprocessing(filepath)
        dataframe['tipo'] = name
        dataframe_to_save = pd.concat([dataframe_to_save, dataframe], ignore_index=True)
        
    filepath_output = os.path.join(directory, 'processamento_out.csv')
    dataframe_to_save.to_csv(filepath_output, index=False, sep=';')
    print(f'Dados pré-processados e salvos para processamento em: {filepath_output}')

if __name__ == '__main__':
    main()
