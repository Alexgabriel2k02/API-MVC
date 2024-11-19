from flask import Blueprint, jsonify
from models import pessoa_model
import logging

pessoa_bp = Blueprint('pessoa_bp', __name__)

@pessoa_bp.route('/professores', methods=['GET'])
def listar_professores():
    try:
        professores = pessoa_model.listar_professores()
        return jsonify(professores)
    except Exception as e:
        logging.error(f"Erro ao listar professores: {e}")
        return jsonify({'erro': 'Erro ao listar professores'}), 500

@pessoa_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    try:
        alunos = pessoa_model.listar_alunos()
        return jsonify(alunos)
    except Exception as e:
        logging.error(f"Erro ao listar alunos: {e}")
        return jsonify({'erro': 'Erro ao listar alunos'}), 500

@pessoa_bp.route('/leciona/<int:id_professor>/<int:id_disciplina>', methods=['GET'])
def verificar_leciona(id_professor: int, id_disciplina: int):
    try:
        leciona = pessoa_model.leciona(id_professor, id_disciplina)
        return jsonify({'leciona': leciona})
    except pessoa_model.DisciplinaNaoEncontrada:
        return jsonify({'erro': 'Disciplina não encontrada'}), 404
    except Exception as e:
        logging.error(f"Erro ao verificar se o professor {id_professor} leciona a disciplina {id_disciplina}: {e}")
        return jsonify({'erro': 'Erro ao verificar leciona'}), 500