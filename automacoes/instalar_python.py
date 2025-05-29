import subprocess
import os
import time


class InstaladorPython:
    def __init__(self, caminho_instalador="downloads/python-3.12.7-amd64.exe"):
        self.caminho_instalador = caminho_instalador

    def verificar_instalador(self):
        """Verifica se o instalador existe no caminho especificado."""
        if not os.path.exists(self.caminho_instalador):
            print(f"Instalador não encontrado: {self.caminho_instalador}")
            return False
        return True

    def executar_instalacao(self):
        """Executa a instalação silenciosa do Python."""
        if not self.verificar_instalador():
            return

        try:
            print("Iniciando a instalação silenciosa...")
            comando = [
                self.caminho_instalador,
                "/quiet",               # instalação silenciosa
                "PrependPath=1",        # adiciona ao PATH
                "Include_test=0"        # não instala arquivos de teste
            ]
            subprocess.run(comando, check=True)
            print("Instalação concluída com sucesso!")
            self.esperar_finalizacao()
        except subprocess.CalledProcessError as erro:
            print(f"Erro durante a instalação: {erro}")

    @staticmethod
    def esperar_finalizacao(tempo=10):
        """Espera alguns segundos para garantir a finalização da instalação."""
        print(f"Aguardando {tempo} segundos para finalizar...")
        time.sleep(tempo)

