
from flask import Flask
from flask_cors import CORS
from routes.adminRoutes import admin
from routes.estudianteRoutes import estudiante
from routes.docenteRoutes import docente
app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(estudiante,url_prefix='/estudiante')
app.register_blueprint(docente,url_prefix='/docente')

UPLOAD_FOLDER ='src/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

CORS(app, origins='http://localhost:4200',supports_credentials=True)
app.secret_key="secret_key"

from controllers.controlador import *


if __name__ == '__main__':
    app.run(debug=True)
