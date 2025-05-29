from logs.mongo_logger import MongoLogger
from automacoes.baixar_python import PythonDownloader
from automacoes.instalar_python import InstaladorPython
from automacoes.verificar_instalacao import PythonChecker

logger = MongoLogger()

try:
    PythonDownloader(download_dir="downloads", versao="3.12.7").executar()
    logger.log("Download", "sucesso", "Python baixado com sucesso")
except Exception as e:
    logger.log("Download", "erro", str(e))

try:
    InstaladorPython().executar_instalacao()
    logger.log("Instalacao", "sucesso", "Python instalado com sucesso")
except Exception as e:
    logger.log("Instalacao", "erro", str(e))

try:
    versao = PythonChecker.verificar_instalacao()
    if versao:
        logger.log("Verificacao", "sucesso", f"Versão instalada: {versao}")
    else:
        logger.log("Verificacao", "erro", "Não foi possível obter a versão")
except Exception as e:
    logger.log("Verificacao", "erro", str(e))
