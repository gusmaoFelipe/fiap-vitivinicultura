from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)
caminho = os.path.abspath(__file__)
diretorio = os.path.dirname(caminho)

# TO-DO: Autenticação

@app.route("/")
def get_root():
    return "API Tech Challenge FIAP"

# Endpoint para extrair dados referente ao menu 'Produção'
@app.route('/api/v1/producao', methods=['GET'])
def get_producao():
    dados_producao = pd.read_csv(diretorio + '/banco_dados/producao.csv', sep=';')
    
    # TO-DO: Mover para uma função
    ano = request.args.get('ano')
    cod_produto = request.args.get('cod_produto')
    if(ano):
        dados_producao = dados_producao[dados_producao['ano'] == int(ano)]
    if cod_produto:
        dados_producao = dados_producao[dados_producao['cod_produto'] == cod_produto]
        
    json_data = dados_producao.to_json(orient='records')
    return jsonify(json_data)


if __name__ == '__main__':
    app.run(debug=True)