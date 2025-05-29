import subprocess

class PythonChecker:
    """Classe para verificar a instalação do Python."""

    @staticmethod
    def verificar_instalacao():
        """Verifica se o Python está instalado e retorna sua versão."""
        try:
            resultado = subprocess.run(
                ["python", "--version"],
                capture_output=True,
                text=True,
                check=True
            )
            versao = resultado.stdout.strip() or resultado.stderr.strip()
            print(f"Python instalado com sucesso: {versao}")
            return versao
        except subprocess.CalledProcessError as erro:
            print(f"Erro ao verificar a versão do Python: {erro}")
            return None


