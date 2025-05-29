import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class PythonDownloader:
    def __init__(self, download_dir="downloads", versao="3.12.7"):
        self.download_dir = os.path.abspath(download_dir)
        self.versao = versao
        self.driver = None

    def configurar_navegador(self):
        """Configura o navegador com as opções necessárias."""
        os.makedirs(self.download_dir, exist_ok=True)
        options = Options()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("prefs", {
            "download.default_directory": self.download_dir,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": True
        })
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def pesquisar_no_google(self):
        """Realiza uma pesquisa no Google pelo site de download do Python."""
        self.driver.get("https://www.google.com")
        time.sleep(1)
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("baixar python site")
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

    def acessar_pagina_download(self):
        """Acessa a página de downloads do site oficial do Python."""
        try:
            link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Downloads")
            link.click()
            time.sleep(2)
        except Exception as e:
            raise Exception("Erro ao acessar a página de downloads: " + str(e))

    def baixar_versao_python(self):
        """Baixa a versão especificada do Python."""
        if self.versao in self.driver.page_source:
            try:
                self.driver.find_element(By.PARTIAL_LINK_TEXT, self.versao).click()
                time.sleep(2)
                self.driver.find_element(By.PARTIAL_LINK_TEXT, "Windows installer (64-bit)").click()
                time.sleep(5)  # Tempo para iniciar o download
            except Exception as e:
                raise Exception("Erro ao baixar a versão do Python: " + str(e))
        else:
            print(f"Versão {self.versao} não encontrada na página.")

    def executar(self):
        """Executa o processo completo de download."""
        try:
            self.configurar_navegador()
            self.pesquisar_no_google()
            self.acessar_pagina_download()
            self.baixar_versao_python()
        except Exception as e:
            print("Erro durante o processo:", e)
        finally:
            if self.driver:
                self.driver.quit()



