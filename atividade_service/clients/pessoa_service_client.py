import requests
import logging
from typing import Optional

PESSOA_SERVICE_URL = "http://localhost:5001/pessoas"

class PessoaServiceClient:
    @staticmethod
    def verificar_leciona(id_professor: int, id_disciplina: int) -> bool:
        url = f"{PESSOA_SERVICE_URL}/leciona/{id_professor}/{id_disciplina}"
        try:
            response = requests.get(url, timeout=10)  # Adicionado timeout
            response.raise_for_status()
            data = response.json()
            return data.get('leciona', False) if data.get('isok') else False
        except requests.RequestException as e:
            logging.error(f"Erro ao acessar o pessoa_service: {e}")  # Substituído print por logging
            return False