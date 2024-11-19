from typing import List, Dict, Any

atividades: List[Dict[str, Any]] = [
    {
        'id_atividade': 1,
        'id_disciplina': 1,
        'enunciado': 'Crie um app de todo em Flask',
        'respostas': [
            {'id_aluno': 1, 'resposta': 'todo.py', 'nota': 9},
            {'id_aluno': 2, 'resposta': 'todo.zip.rar'},
            {'id_aluno': 4, 'resposta': 'todo.zip', 'nota': 10}
        ]
    },
    {
        'id_atividade': 2,
        'id_disciplina': 1,
        'enunciado': 'Crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta': 'email.zip', 'nota': 10}
        ]
    }
]

class AtividadeNotFound(Exception):
    def __init__(self, id_atividade: int):
        self.id_atividade = id_atividade
        super().__init__(f"Atividade com id {id_atividade} não encontrada")

def listar_atividades() -> List[Dict[str, Any]]:
    return atividades

def obter_atividade(id_atividade: int) -> Dict[str, Any]:
    atividade = next((a for a in atividades if a['id_atividade'] == id_atividade), None)
    if atividade is None:
        raise AtividadeNotFound(id_atividade)
    return atividade

def adicionar_atividade(atividade: Dict[str, Any]) -> None:
    atividades.append(atividade)

def atualizar_atividade(id_atividade: int, novos_dados: Dict[str, Any]) -> None:
    atividade = obter_atividade(id_atividade)
    atividade.update(novos_dados)

def excluir_atividade(id_atividade: int) -> None:
    global atividades
    atividades = [a for a in atividades if a['id_atividade'] != id_atividade]