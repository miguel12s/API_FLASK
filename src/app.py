from flask import Flask, jsonify, request
from models.estudiante import Estudiante
from models.user import User
from models.modelos import insertarUsuario, insertarEstudiante, searchUserForRol,getPasswordHash
from utils.Security import Security


app = Flask(__name__)


@app.route('/')
def index():

    return jsonify('bienvenido')


@app.route('/registro', methods=['POST'])
def registro():
    response = {}

    try:
        data: Estudiante = request.json
        if not data:
            response = {'message': 'no hay datos en la request'}
            status = 400
        return jsonify(response, status, data)

    except Exception as e:
        response = {'message': 'solicitud procesada'}
        status = 200
        user = User('1', '1', data['correo'], data['contraseña'])
        print("la contraseña hasheada es "+user.contraseña)
        id_usuario = insertarUsuario(user)
        estudiante = Estudiante(id_usuario, data['nombre'], data['apellido'], data['tipoDocumento'],
                                data['numeroDocumento'], data['celular'], data['programa'], data['facultad'], data['correo'])
        insertarEstudiante(estudiante)

        return jsonify(response, status, data)


@app.route('/login', methods=['post'])
def login():
    id_usuario: int
    id_rol: int
    data = request.json
    message={}
    
    if not data:

        return jsonify('los datos estan incorrectos')
    passwordHashed=getPasswordHash(data['correo'])
    if(passwordHashed!=None):
        id_usuario, id_rol = searchUserForRol(passwordHashed,data)
        if(id_usuario!=False):
            if (id_rol != None):
                token = Security.generateToken(id_usuario)
                message=({"success": True, token: token})
            else:
                message=({"success":False})
                
        else:
         message=({"success":False})

        return jsonify(message)    
    else:
        return jsonify(message)  

if __name__ == '__main__':
    app.run(debug=True)
