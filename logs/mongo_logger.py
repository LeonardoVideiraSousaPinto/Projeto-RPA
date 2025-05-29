from pymongo import MongoClient
from datetime import datetime

class MongoLogger:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="rpa_logs", collection_name="execucoes"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def log(self, etapa, status, mensagem):
        log_entry = {
            "etapa": etapa,
            "status": status,
            "mensagem": mensagem,
            "data_execucao": datetime.now()
        }
        self.collection.insert_one(log_entry)
        print(f"Log registrado: [{etapa}] - {status}")
