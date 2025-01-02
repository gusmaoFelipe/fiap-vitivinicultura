# fiap-vitivinicultura


Utilizando o VSCode, criar um ambiente virtual no 'mesmo nível' do projeto fiap-vitivinicultura

Exemplo:

FIAP\
    .venv\
        ...
    fiap-vitivinicultura\
        ...

Na pasta FIAP, ativar o ambiente virtual:

source .venv/bin/activate

Instalar as bibliotecas necessárias no ambiente virtual:

pip install -r requirements.txt

Iniciando o serviço no ambiente virtual

python3 fiap-vitivinicultura/app.py

Requisitando os dados de 'Produção' para o ano de 2023 utilizando um client qualquer (Postman):

http://127.0.0.1:5000/api/v1/producao?ano=2023

Resultado


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
    {
        "cod_produto": "vinho_mesa_branco",
        "produto": "BRANCO",
        "ano": 2023,
        "litros": 27910299
    },
    {
        "cod_produto": "vinho_mesa_rosado",
        "produto": "ROSADO",
        "ano": 2023,
        "litros": 2531246
    },
    {
        "cod_produto": "vinho_fino_de_mesa_vinifera",
        "produto": "VINHO FINO DE MESA (VINIFERA)",
        "ano": 2023,
        "litros": 46268556
    },
    {
        "cod_produto": "vinho_viniferas_tinto",
        "produto": "TINTO",
        "ano": 2023,
        "litros": 23615783
    },
    {
        "cod_produto": "vinho_viniferas_branco",
        "produto": "BRANCO",
        "ano": 2023,
        "litros": 20693437
    },
    {
        "cod_produto": "vinho_viniferas_rosado",
        "produto": "ROSADO",
        "ano": 2023,
        "litros": 1959336
    },
    {
        "cod_produto": "suco",
        "produto": "SUCO",
        "ano": 2023,
        "litros": 67045238
    },
    {
        "cod_produto": "suco_de_uva_simples",
        "produto": "SUCO DE UVA INTEGRAL",
        "ano": 2023,
        "litros": 38122173
    },
    {
        "cod_produto": "suco_concentrado",
        "produto": "SUCO DE UVA CONCENTRADO",
        "ano": 2023,
        "litros": 28216760
    },
    {
        "cod_produto": "suco_de_uva_adocado",
        "produto": "SUCO DE UVA ADOÇADO",
        "ano": 2023,
        "litros": 94587
    },
    {
        "cod_produto": "suco_de_uva_organico",
        "produto": "SUCO DE UVA ORGÂNICO",
        "ano": 2023,
        "litros": 611718
    },
    {
        "cod_produto": "suco_de_uva_reconstituido",
        "produto": "SUCO DE UVA RECONSTITUÍDO",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados",
        "produto": "DERIVADOS",
        "ano": 2023,
        "litros": 174716647
    },
    {
        "cod_produto": "derivados_espumante",
        "produto": "ESPUMANTE",
        "ano": 2023,
        "litros": 65525
    },
    {
        "cod_produto": "derivados_espumante_moscatel",
        "produto": "ESPUMANTE MOSCATEL",
        "ano": 2023,
        "litros": 14744
    },
    {
        "cod_produto": "derivados_base_espumante",
        "produto": "BASE ESPUMANTE",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_base_espumante_moscatel",
        "produto": "BASE ESPUMANTE MOSCATEL",
        "ano": 2023,
        "litros": 6734590
    },
    {
        "cod_produto": "derivados_base_champenoise_champanha",
        "produto": "BASE CHAMPENOISE CHAMPANHA",
        "ano": 2023,
        "litros": 1552243
    },
    {
        "cod_produto": "derivados_base_charmat_champanha",
        "produto": "BASE CHARMAT CHAMPANHA",
        "ano": 2023,
        "litros": 5418118
    },
    {
        "cod_produto": "derivados_bebida_de_uva",
        "produto": "BEBIDA DE UVA",
        "ano": 2023,
        "litros": 1627
    },
    {
        "cod_produto": "derivados_polpa_de_uva",
        "produto": "POLPA DE UVA",
        "ano": 2023,
        "litros": 1388251
    },
    {
        "cod_produto": "derivados_mosto_simples",
        "produto": "MOSTO SIMPLES",
        "ano": 2023,
        "litros": 157848983
    },
    {
        "cod_produto": "derivados_mosto_concentrado",
        "produto": "MOSTO CONCENTRADO",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_mosto_de_uva_com_bagaco",
        "produto": "MOSTO DE UVA COM BAGAÇO",
        "ano": 2023,
        "litros": 7784
    },
    {
        "cod_produto": "derivados_mosto_dessulfitado",
        "produto": "MOSTO DESSULFITADO",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_mistelas",
        "produto": "MISTELAS",
        "ano": 2023,
        "litros": 600
    },
    {
        "cod_produto": "derivados_nectar_de_uva",
        "produto": "NÉCTAR DE UVA",
        "ano": 2023,
        "litros": 70976
    },
    {
        "cod_produto": "derivados_licorosos",
        "produto": "LICOROSOS",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_compostos",
        "produto": "COMPOSTOS",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_jeropiga",
        "produto": "JEROPIGA",
        "ano": 2023,
        "litros": 4500
    },
    {
        "cod_produto": "derivados_filtrado",
        "produto": "FILTRADO",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_frisante",
        "produto": "FRISANTE",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_vinho_leve",
        "produto": "VINHO LEVE",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_vinho_licoroso",
        "produto": "VINHO LICOROSO",
        "ano": 2023,
        "litros": 73600
    },
    {
        "cod_produto": "derivados_brandy",
        "produto": "BRANDY",
        "ano": 2023,
        "litros": 450
    },
    {
        "cod_produto": "derivados_destilado",
        "produto": "DESTILADO",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_bagaceira",
        "produto": "BAGACEIRA",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_licor_de_bagaceira",
        "produto": "LICOR DE BAGACEIRA",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_vinagre",
        "produto": "VINAGRE",
        "ano": 2023,
        "litros": 9000
    },
    {
        "cod_produto": "derivados_borra_liquida",
        "produto": "BORRA LÍQUIDA",
        "ano": 2023,
        "litros": 758140
    },
    {
        "cod_produto": "derivados_borra_seca",
        "produto": "BORRA SECA",
        "ano": 2023,
        "litros": 17200
    },
    {
        "cod_produto": "derivados_vinho_composto",
        "produto": "VINHO COMPOSTO",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_pisco",
        "produto": "PISCO",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_vinho_organico",
        "produto": "VINHO ORGÂNICO",
        "ano": 2023,
        "litros": 94150
    },
    {
        "cod_produto": "derivados_espumante_organico",
        "produto": "ESPUMANTE ORGÂNICO",
        "ano": 2023,
        "litros": 1365
    },
    {
        "cod_produto": "derivados_destilado_alcoolico_simples_de_bagaceira_",
        "produto": "DESTILADO ALCOÓLICO SIMPLES DE BAGACEIRA ",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_vinho_acidificado_",
        "produto": "VINHO ACIDIFICADO ",
        "ano": 2023,
        "litros": 2500
    },
    {
        "cod_produto": "derivados_mosto_parcialmente_fermentado_",
        "produto": "MOSTO PARCIALMENTE FERMENTADO ",
        "ano": 2023,
        "litros": 0
    },
    {
        "cod_produto": "derivados_outros_derivados",
        "produto": "OUTROS DERIVADOS",
        "ano": 2023,
        "litros": 652301
    }
]