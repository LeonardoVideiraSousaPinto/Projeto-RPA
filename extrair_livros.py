from automacoes.extrair_dados import RaspadorLivros
from automacoes.gerar_relatorio import GeradorRelatorioLivros


def main():
    try:
        # Etapa 1: Inicializar o raspador de livros e raspar dados
        raspador = RaspadorLivros()
        print("Iniciando raspagem de dados...")
        raspador.raspar_tudo()
        print("Raspagem concluída. Salvando dados em CSV...")
        raspador.salvar_csv()
        print("Dados salvos com sucesso.")

        # Etapa 2: Inicializar o gerador de relatório e processar dados
        relatorio = GeradorRelatorioLivros()
        print("Carregando dados para o relatório...")
        relatorio.carregar_dados()
        print("Processando dados...")
        relatorio.processar_dados()
        print("Gerando relatório em PDF...")
        relatorio.gerar_pdf()
        print("Relatório gerado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == '__main__':
    main()
