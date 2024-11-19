from flask import Blueprint, jsonify, request
from models.atividade_model import AtividadeNotFound, listar_atividades, obter_atividade, adicionar_atividade, atualizar_atividade, excluir_atividade
from clients.pessoa_service_client import PessoaServiceClient
import logging

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/', methods=['GET'])
def atividades():
    try:
        atividades = listar_atividades()
        return jsonify(atividades)
    except Exception as e:
        logging.error(f"Erro ao listar atividades: {e}")
        return jsonify({'erro': 'Erro ao listar atividades'}), 500

@atividade_bp.route('/<int:id_atividade>', methods=['GET'])
def atividade_id(id_atividade: int):
    try:
        atividade = obter_atividade(id_atividade)
        return jsonify(atividade)
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    except Exception as e:
        logging.error(f"Erro ao obter atividade {id_atividade}: {e}")
        return jsonify({'erro': 'Erro ao obter atividade'}), 500

@atividade_bp.route('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
def obter_atividade_para_professor(id_atividade: int, id_professor: int):
    try:
        atividade = obter_atividade(id_atividade)
        if not PessoaServiceClient.verificar_leciona(id_professor, atividade['id_disciplina']):
            atividade = atividade.copy()
            atividade.pop('respostas', None)
        return jsonify(atividade)
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    except Exception as e:
        logging.error(f"Erro ao obter atividade {id_atividade} para professor {id_professor}: {e}")
        return jsonify({'erro': 'Erro ao obter atividade para professor'}), 500

@atividade_bp.route('/', methods=['POST'])
def add_atividade():
    data = request.json
    try:
        adicionar_atividade(data)
        return jsonify({'mensagem': 'Atividade adicionada com sucesso'}), 201
    except Exception as e:
        logging.error(f"Erro ao adicionar atividade: {e}")
        return jsonify({'erro': 'Erro ao adicionar atividade'}), 500

@atividade_bp.route('/<int:id_atividade>', methods=['PUT'])
def atualizar_atividade(id_atividade: int):
    data = request.json
    try:
        atualizar_atividade(id_atividade, data)
        return jsonify(obter_atividade(id_atividade)), 200
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    except Exception as e:
        logging.error(f"Erro ao atualizar atividade {id_atividade}: {e}")
        return jsonify({'erro': 'Erro ao atualizar atividade'}), 500

@atividade_bp.route('/<int:id_atividade>', methods=['DELETE'])
def deletar_atividade(id_atividade: int):
    try:
        excluir_atividade(id_atividade)
        return '', 204
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404
    except Exception as e:
        logging.error(f"Erro ao deletar atividade {id_atividade}: {e}")
        return jsonify({'erro': 'Erro ao deletar atividade'}), 500