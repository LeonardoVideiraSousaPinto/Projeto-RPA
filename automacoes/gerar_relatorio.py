import pandas as pd
from fpdf import FPDF
import os


class GeradorRelatorioLivros:
    def __init__(self, caminho_csv='data/livros.csv', caminho_pdf='data/relatorio_livros.pdf'):
        self.caminho_csv = caminho_csv
        self.caminho_pdf = caminho_pdf
        self.df = None
        self.resumo = None

    def carregar_dados(self):
        if not os.path.exists(self.caminho_csv):
            raise FileNotFoundError(f"Arquivo CSV não encontrado: {self.caminho_csv}")
        self.df = pd.read_csv(self.caminho_csv)
        print("Dados carregados com sucesso.")

    def processar_dados(self):
        self.df['preco'] = self.df['preco'].replace('Â£', '', regex=True).astype(float)
        self.resumo = self.df.groupby('categoria').agg(
            total_livros=('titulo', 'count'),
            media_preco=('preco', 'mean'),
            em_estoque=('em_estoque', 'sum')
        ).reset_index()
        self.resumo = self.resumo.sort_values(by='total_livros', ascending=False)
        print("Dados processados com sucesso.")

    def gerar_pdf(self):
        if self.resumo is None:
            raise ValueError("Dados não processados. Execute 'processar_dados' primeiro.")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Relatório Resumido de Livros", ln=True, align='C')
        pdf.ln(10)

        colunas = ["Categoria", "Total de Livros", "Média de Preço (£)", "Em Estoque"]
        larguras = [60, 40, 50, 40]

        for i in range(len(colunas)):
            pdf.cell(larguras[i], 10, colunas[i], border=1)
        pdf.ln()

        for _, linha in self.resumo.iterrows():
            pdf.cell(larguras[0], 10, str(linha['categoria']), border=1)
            pdf.cell(larguras[1], 10, str(linha['total_livros']), border=1)
            pdf.cell(larguras[2], 10, f"{linha['media_preco']:.2f}", border=1)
            pdf.cell(larguras[3], 10, str(linha['em_estoque']), border=1)
            pdf.ln()

        os.makedirs(os.path.dirname(self.caminho_pdf), exist_ok=True)
        pdf.output(self.caminho_pdf)
        print(f"Relatório gerado em: {self.caminho_pdf}")


