from processa_producao_comercializacao import main as processa_producao_comercializacao
from processa_processamento import main as processa_processamento
from processa_importacao_exportacao import main as processa_importacao_exportacao

def main():
    processa_producao_comercializacao()
    processa_processamento()
    processa_importacao_exportacao()

if __name__ == "__main__":
    main()