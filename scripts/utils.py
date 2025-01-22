from unicodedata import normalize
import os
import requests

def download_csv(url, diretorio, nome):
    os.makedirs(diretorio, exist_ok=True)
    caminho = os.path.join(diretorio, nome)
    resposta = requests.get(url)
    
    if os.path.exists(caminho):
        os.remove(caminho)

    if resposta.status_code == 200:
        with open(caminho, 'wb') as arquivo:
            arquivo.write(resposta.content)
    else:
        print(f'Erro: {resposta.status_code}')
    
    return caminho

def remover_acentos(texto):
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

def normalizar_dataframe(dataframe, dicionario_substituicoes):
    dataframe = dataframe.apply(lambda x: x.astype(str).str.lower())
    dataframe.columns = map(str.lower, dataframe.columns)
    dataframe = dataframe.replace(to_replace=dicionario_substituicoes, regex=True)
    return dataframe