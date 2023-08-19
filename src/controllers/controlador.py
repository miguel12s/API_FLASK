from app import app
from flask import jsonify, request, send_from_directory
from models.modelosSimples import getPrograms, getTipoDocumento, getSedes, getMaterias, getSalon, getEstadoTutoria, existEmail,getFacultades
from models.estudiante import Estudiante
from models.user import User
from databases.conexion import getConecction
from models.modelos import getPasswordHash, searchUserForRol, getPasswordForId, updatePassword, getIdRol
from models.horario import Horario
from models.horario_modelos import getTutoriaForId
from models.docente import Docente
from models import consultasHorario
from models.consultasHorario import consultasHorario
from models.forgot import Forgot
from models.modelosAdmin import ModelosAdmin
from utils.Security import Security
from services.Mail import send_email
import os
from werkzeug.utils import secure_filename


bd = getConecction()
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower()


@app.route("/upload", methods=["POST"])
def upload():

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
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
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


@app.route('/display/<filename>')
def display(filename):

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/salon',)
def salon():
    salon = getSalon()
    return jsonify(salon)


@app.route('/estadoTutoria')
def estadoTutoria():
    estado = getEstadoTutoria()
    return jsonify(estado)


@app.route('/materias')
def materias():
    materias = getMaterias()
    return jsonify(materias)


@app.route('/tipo-documento')
def tipoDocumento():
    tipoDocumento = getTipoDocumento()
    return jsonify(tipoDocumento)


@app.route('/sedes')
def sedes():
    sedes = getSedes()
    return jsonify(sedes)


@app.route('/programas')
def programas():
    programas = getPrograms()
    return jsonify(programas)


@app.route('/facultades')
def facultades():
    facultades = getFacultades()
    print(facultades)
    return jsonify(facultades)



@app.route('/login', methods=['post'])
def login():

    message = {}
    data = request.json
    if not data:
        return jsonify({'message': "no hay datos en la request"})

    passwordHashed = getPasswordHash(data['correo'])

    if (passwordHashed != None):
        id_usuario, id_rol, id_estado = searchUserForRol(passwordHashed, data)
        if (id_usuario != False):
            print(id_usuario)
            if (id_rol != None):

                token = Security.generateToken(id_usuario)
                message = ({"success": True, 'token': token, "rol": id_rol,
                           "usuario": id_usuario, "id_estado": id_estado})
            else:
                message = ({"success": False})
        else:
            message = ({"success": False})
        return jsonify(message)
    else:
        return jsonify(message)


# @app.route('/logout')

# def logout():
#     return jsonify({'message': 'Cierre de sesión exitoso'})


# @app.route('/protected')

# def protected():
#     return jsonify({'message':"ruta protegida"})

@app.route('/cambiar-contraseña', methods=['post'])
def cambiar_contraseña():
    response = request.json
    headers = request.headers
    payload = Security.verify_token(headers)
    id_usuario = payload.get('id_usuario')
    contraseña = response['contraseña'],
    nuevaContraseña = response['nuevaContraseña']
    hashedPassword = getPasswordForId(id_usuario)
    if (User.checkPassword(hashedPassword, contraseña[0])):
        newPassword = User.generatePassword(nuevaContraseña)
        updatePassword(id_usuario, newPassword)

        return jsonify({"message": "la contraseña ha sido cambiada"})
    return jsonify({"message": "la contraseña no ha sido cambiada"})


@app.route('/obtenerCapacidad', methods=['post'])
def obtenerCapacidad():

    data = request.json
    id_salon, id_capacidad, id_sede = Horario.obtenerSalon(data['salon'])
    print(id_salon, id_capacidad, id_sede)

    capacidad = Horario.obtenerCapacidad(id_capacidad)

    return jsonify({"data": capacidad})


@app.route('/forgot', methods=['post'])
def forgot():
    data = request.json
    print(data)
    email = data['email']
    if (email != ""):
        number = existEmail(email)
        print(number)
        existe = True if number == 1 else False
        if (existe):
            forgot = Forgot(bd)
            password = forgot.getPassword()
            print(password)
            subject = 'Cambio de contraseña'
            body = f'la contraseña es {password}'
            send_email(subject, body, email)
            passwordHash = forgot.generatePasswordHash(password)
            print(password, passwordHash)
            forgot.updatePassword(email, passwordHash)

            return jsonify({"success": "la contraseña ha sido cambiada"})
        return jsonify({"message": 'el correo no existe en el sistema'})
    return jsonify({"message": "correo invalido"})

    # if not logout:
    #     return jsonify({"message":"error"})

# @app.route('/renew-token', methods=['POST'])
# def renew_token():
#     data = request.get_json()
#     token = data.get('token')  # Token a renovar

#     if token:
#         new_token = Security.renew_token(token)
#         if new_token:
#             return jsonify({'new_token': new_token}), 200
#         else:
#             return jsonify({'message': 'Token renewal failed'}), 401
#     else:
#         return jsonify({'message': 'Token not provided'}), 400


@app.route('/buscarPrograma/<facultad>')
def buscarProgramas(facultad):
    modelo = ModelosAdmin(bd)
    id_facultad = modelo.obtenerIdFacultad(facultad)
    programas = modelo.buscarProgramas(id_facultad)
    print(programas)
    return jsonify({"data": programas}), 201

@app.route('/obtenerTutoria/<id_tutoria>', methods=['get'])
def obtenerTutoria(id_tutoria):
    tutoria = getTutoriaForId(id_tutoria)
    horario = consultasHorario.serializeTutoria(tutoria)
    return jsonify({"data": horario})
