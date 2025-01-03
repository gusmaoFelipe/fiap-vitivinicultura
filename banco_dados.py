import pandas as pd
import os

caminho = os.path.abspath(__file__)
diretorio = os.path.dirname(caminho)

# TO-DO: Refatorar para reusar código

# Processa os dados do menu 'Produção' (producao.csv) e cria um banco de dados normalizado
def producao():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    # TO-DO: fazer o download do arquivo no site e, caso não encontre, processar o csv da
    # pasta 'dados_embrapa'
    dados_embrapa_producao = pd.read_csv(
        diretorio + "/dados_embrapa/producao.csv", sep=";"
    )
    # Remove as colunas que não serão utilizadas
    dados_embrapa_producao = dados_embrapa_producao.drop(columns=["id"])
    # Renomeia o campo 'control' para 'cod_produto'
    dados_embrapa_producao.rename(columns={"control": "cod_produto"}, inplace=True)

    # Modifica todos valores de 'cod_produto' para lowercase e 'produto' para uppercase
    dados_embrapa_producao["cod_produto"] = dados_embrapa_producao[
        "cod_produto"
    ].str.lower()
    dados_embrapa_producao["produto"] = dados_embrapa_producao["produto"].str.upper()
    # Normaliza os dados para torna-los mais legíveis
    caracteres_substituir = {
        "vm_": "vinho_mesa_",
        "vv_": "vinho_viniferas_",
        "su_": "",  # palara suco já existe no cod_produto
        "de_": "derivados_",
        "ve_": "vinho_especial_",
        "\(": "",
        "\)": "",
        "â": "a",
        "ç": "c",
        "é": "e",
        "í": "i",
        "ó": "o",
        " ": "_",
    }
    dados_embrapa_producao["cod_produto"] = dados_embrapa_producao[
        "cod_produto"
    ].replace(to_replace=caracteres_substituir, regex=True)

    # Pivota os dados de produção, transformando os anos em 'observações'
    banco_dados_producao = dados_embrapa_producao.melt(
        id_vars=["cod_produto", "produto"], var_name="ano", value_name="litros"
    )
    # Salva os dados pivotados de produção em um novo CSV para ser posteriormente utilizado pela API
    banco_dados_producao.to_csv(
        diretorio + "/banco_dados/producao.csv", sep=";", index=False
    )
    print("Dados do menu 'Produção' processados com sucesso e banco de dados criado.")



#  Processa os dados do menu 'Comercialização' (comercio.csv) e cria um banco de dados normalizado
def comercio():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
    # TO-DO: fazer o download do arquivo no site e, caso não encontre, processar o csv da
    # pasta 'dados_embrapa'
    dados_embrapa_comercio = pd.read_csv(
        diretorio + "/dados_embrapa/comercio.csv", sep=";"
    )
    # Remove as colunas que não serão utilizadas
    dados_embrapa_comercio = dados_embrapa_comercio.drop(columns=["id"])
    # Renomeia o campo 'control' para 'cod_produto'
    dados_embrapa_comercio.rename(columns={"control": "cod_produto", "Produto": "produto"}, inplace=True)

    # Modifica todos valores de 'cod_produto' para lowercase e 'produto' para uppercase
    dados_embrapa_comercio["cod_produto"] = dados_embrapa_comercio[
        "cod_produto"
    ].str.lower()
    dados_embrapa_comercio["produto"] = dados_embrapa_comercio["produto"].str.upper()
    dados_embrapa_comercio["produto"] = dados_embrapa_comercio["produto"].str.strip()

    # Normaliza os dados para torna-los mais legíveis
    caracteres_substituir = {
        "vm_": "vinho_mesa_",
        "vv_": "vinho_viniferas_",
        "su_": "",  # palara 'suco' já existe no cod_produto
        "de_": "derivados_",
        "ve_": "vinho_especial_",
        "es_": "", # palavra 'espumante' já existe no cod_produto
        "ou_": "outro_",
        "\(": "",
        "\)": "",
        "â": "a",
        "ç": "c",
        "é": "e",
        "í": "i",
        "ó": "o",
        " ": "_",
    }
    dados_embrapa_comercio["cod_produto"] = dados_embrapa_comercio[
        "cod_produto"
    ].replace(to_replace=caracteres_substituir, regex=True)

    # Pivota os dados de produção, transformando os anos em 'observações'
    banco_dados_comercio = dados_embrapa_comercio.melt(
        id_vars=["cod_produto", "produto"], var_name="ano", value_name="litros"
    )
    # Salva os dados pivotados de produção em um novo CSV para ser posteriormente utilizado pela API
    banco_dados_comercio.to_csv(
        diretorio + "/banco_dados/comercio.csv", sep=";", index=False
    )
    print("Dados do menu 'Comercialização' processados com sucesso e banco de dados criado.")


def main():
    producao()
    comercio()


if __name__ == "__main__":
    main()
