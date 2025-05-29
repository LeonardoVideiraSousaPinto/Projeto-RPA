import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

class RaspadorLivros:
    URL_BASE = 'https://books.toscrape.com/'

    def __init__(self):
        self.sessao = requests.Session()
        self.livros = []

    def obter_dados_bs4(self, caminho: str) -> BeautifulSoup:
        resposta = self.sessao.get(self.URL_BASE + caminho)
        return BeautifulSoup(resposta.text, 'html.parser')

    def obter_categorias(self):
        sopa = self.obter_dados_bs4('index.html')
        elementos = sopa.select(
            '#default > div > div > div > aside > div:nth-of-type(2) > ul > li > ul > li > a'
        )
        return [(el.text.strip(), el['href']) for el in elementos]

    def extrair_info_livro(self, livro_html, categoria):
        titulo = livro_html.find('h3').find('a')['title']
        preco = livro_html.select_one('.price_color').text.strip()
        em_estoque = 'In stock' in livro_html.select_one('.instock').text.strip()
        return {
            'titulo': titulo,
            'preco': preco,
            'em_estoque': em_estoque,
            'categoria': categoria
        }

    def raspar_categoria(self, nome_categoria, url_categoria):
        pagina = 1
        while True:
            partes = url_categoria.split('/')[:-1]
            caminho = '/'.join(partes) + f'/page-{pagina}.html' if pagina > 1 else url_categoria
            sopa = self.obter_dados_bs4(caminho)

            livros_html = sopa.select('.product_pod')
            if not livros_html:
                break

            for livro_html in livros_html:
                livro = self.extrair_info_livro(livro_html, nome_categoria)
                self.livros.append(livro)

            paginador = sopa.select_one('.current')
            if not paginador or pagina >= int(paginador.text.strip().split()[-1]):
                break
            pagina += 1

    def raspar_tudo(self):
        categorias = self.obter_categorias()
        for nome, href in categorias:
            print(f"Raspando categoria: {nome}")
            self.raspar_categoria(nome, href)

    def salvar_csv(self, nome_arquivo='data/livros.csv'):
        df = pd.DataFrame(self.livros)
        os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
        df.to_csv(nome_arquivo, index=False, encoding='utf-8-sig')
        print(f"Dados salvos em: {nome_arquivo}")

