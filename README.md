# fiap-vitivinicultura

Repositório com a implementação da Fase 01 do Tech Challenge de Machine Learning Enginnering da FIAP.
Autores: André Santos e Felipe Gusmão.



Instalação e Execução

Utilizando o VSCode, criar um ambiente virtual no 'mesmo nível' do projeto fiap-vitivinicultura

Exemplo:

```
FIAP\
    .venv\
        ...
    fiap-vitivinicultura\
        ...
```

Na pasta FIAP, ativar o ambiente virtual:

```
source .venv/bin/activate
```

Instalar as bibliotecas necessárias no ambiente virtual:

```
pip install -r requirements.txt
```

Iniciando o serviço no ambiente virtual

```
python3 fiap-vitivinicultura/app.py
```

Requisitando os dados de 'Produção' para o ano de 2023:

```
http://127.0.0.1:5000/api/v1/producao?ano=2023
```

Resultado

```JSON
    [
        {
            "cod_produto": "vinho_de_mesa",
            "produto": "VINHO DE MESA",
            "ano": 2023,
            "litros": 169762429
        },
        {
            "cod_produto": "vinho_mesa_tinto",
            "produto": "TINTO",
            "ano": 2023,
            "litros": 139320884
        },
        ...
    ]
```


Requisitando os dados de 'Comercialização' para o ano de 2022:

```
http://127.0.0.1:5000/api/v1/comercio?ano=2022
```

Resultado

```JSON
    [
        {
            "cod_produto": "vinho_de_mesa",
            "produto": "VINHO DE MESA",
            "ano": 2022,
            "litros": 187939996
        },
        {
            "cod_produto": "vinho_mesa_tinto",
            "produto": "TINTO",
            "ano": 2022,
            "litros": 165067340
        },
        ...
    ]
```