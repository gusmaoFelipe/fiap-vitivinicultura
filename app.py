from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)
caminho = os.path.abspath(__file__)
diretorio = os.path.dirname(caminho)

producao = 'producao'
comercializacao = 'comercializacao'
processamento = 'processamento'
importacao = 'importacao'
exportacao = 'exportacao'
api_head = '/api/v1/'

# TO-DO: Autenticação

def apply_filters(data, ano=None, cod_produto=None, control=None, pais=None, tipo=None):
    
    if ano:
        data = data[data['ano'] == int(ano)]
    if cod_produto:
        data = data[data['cod_produto'] == cod_produto]
    if control:
        data = data[data['control'] == control]    
    if pais:
        data = data[data['pais'] == pais]
    if tipo:
        data = data[data['tipo'] == tipo]
                
    return data

def extract_csv(name):
    return pd.read_csv(diretorio + f'/data/{name}_out.csv', sep=';')
    
def convert_json(data):
    return data.to_json(orient='records')
    
@app.route("/")
def get_root():
    return "API Tech Challenge FIAP"

@app.route(f'{api_head}{producao}', methods=['GET'])
def get_producao():
    dataframe = pd.read_csv(diretorio + f'/data/producao_out.csv', sep=';')
    dataframe = apply_filters(dataframe, ano=request.args.get('ano'), cod_produto=request.args.get('cod_produto')) 
    return convert_json(dataframe)

@app.route(f'{api_head}{comercializacao}', methods=['GET'])
def get_comercializacao():
    dataframe = extract_csv(comercializacao)
    dataframe = apply_filters(dataframe, ano=request.args.get('ano'), cod_produto=request.args.get('cod_produto')) 
    return convert_json(dataframe)

@app.route(f'{api_head}{processamento}', methods=['GET'])
def get_processamento():
    dataframe = extract_csv(processamento)
    dataframe = apply_filters(dataframe, 
                              ano=request.args.get('ano'), 
                              pais=request.args.get('pais'),
                              tipo=request.args.get('tipo')) 
    return convert_json(dataframe)
    
@app.route(f'{api_head}{importacao}', methods=['GET'])
def get_importacao():
    dataframe = extract_csv(importacao)
    dataframe = apply_filters(dataframe, 
                              ano=request.args.get('ano'), 
                              pais=request.args.get('pais'),
                              tipo=request.args.get('tipo')) 
    return convert_json(dataframe)
    
@app.route(f'{api_head}{exportacao}', methods=['GET'])
def get_exportacao():
    dataframe = extract_csv(exportacao)
    dataframe = apply_filters(dataframe, 
                              ano=request.args.get('ano'), 
                              pais=request.args.get('pais'),
                              tipo=request.args.get('tipo')) 
    return convert_json(dataframe)


if __name__ == '__main__':
    app.run(port=8000, debug=True)