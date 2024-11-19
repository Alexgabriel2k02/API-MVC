import requests
import logging
from typing import Tuple

PESSOA_SERVICE_URL = "http://localhost:5001"

def verifica_leciona(id_professor: int, id_disciplina: int) -> Tuple[bool, str]:
    try:
        r = requests.get(f"{PESSOA_SERVICE_URL}/leciona/{id_professor}/{id_disciplina}", timeout=5)
        if r.status_code == 404:
            return False, 'Disciplina não encontrada'
        return r.json().get('leciona', False), ''
    except requests.RequestException as e:
        logging.error(f"Erro na comunicação com pessoa_service: {e}")
        return False, f"Erro na comunicação com pessoa_service: {e}"