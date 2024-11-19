from typing import Any, List, Dict

class DisciplinaNaoEncontrada(Exception):
    def __init__(self, id_disciplina: int):
        self.id_disciplina = id_disciplina
        super().__init__(f"Disciplina com id {id_disciplina} não encontrada")

def leciona(id_professor: int, id_disciplina: int) -> bool:
    disciplinas: List[Dict[str, Any ]] = [
        # Exemplo de estrutura de dados de disciplinas
        {
            'id_disciplina': 1,
            'professores': [1, 2, 3]
        },
        {
            'id_disciplina': 2,
            'professores': [2, 3, 4]
        }
    ]

    for disciplina in disciplinas:
        if disciplina['id_disciplina'] == id_disciplina:
            return id_professor in disciplina['professores']
    raise DisciplinaNaoEncontrada(id_disciplina)