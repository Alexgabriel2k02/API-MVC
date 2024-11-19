import logging
from config import create_app
from controllers.atividade_controller import atividade_bp

logging.basicConfig(level=logging.INFO)

app = create_app()
app.register_blueprint(atividade_bp, url_prefix='/atividades')

if __name__ == '__main__':
    import os
    host = os.getenv('FLASK_RUN_HOST', 'localhost')
    port = int(os.getenv('FLASK_RUN_PORT', 5002))
    app.run(host=host, port=port)