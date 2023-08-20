from flask import jsonify,Blueprint,request, send_from_directory,current_app
import os
from models.docente import Docente
from models.estudiante import Estudiante
from models.modelos import getIdRol
from werkzeug.utils import secure_filename
from utils.Security import Security
upload_blueprint=Blueprint('upload',__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower()


@upload_blueprint.route("", methods=["POST"])
def uploadFile():

    verify = request.headers
    print(verify)
    payload = Security.verify_token(verify)
    print(payload)
    id_usuario = payload['id_usuario']

    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró el archivo'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nombre de archivo no válido'}), 400

    filename = secure_filename(file.filename)
    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    image_path = os.path.join('', filename)
    rol = getIdRol(id_usuario)
    print(rol)
    if (rol == 1):
        Estudiante.updateImage(filename, id_usuario)
        print(image_path)
        estudiante = Estudiante.get(id_usuario)
        response = jsonify({'message': 'Archivo subido correctamente',
                           'imgPath': image_path, 'datos': estudiante.serialize()})

    elif (rol == 2):
        Docente.updateImage(filename, id_usuario)
        docente = Docente.get(id_usuario)
        response = jsonify({'message': 'Archivo subido correctamente',
                           'imgPath': image_path, 'datos': docente.serialize()})

    return response, 200


@upload_blueprint.route('/display/<filename>')
def display(filename):

    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


