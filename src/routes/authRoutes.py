from flask import Blueprint, jsonify,request

from models.modelos import getPasswordHash, searchUserForRol
from databases.conexion import getConecction
from models.forgot import Forgot
from models.modelos import getPasswordForId, updatePassword
from models.modelosSimples import existEmail
from models.user import User
from services.Mail import send_email
from utils.Security import Security


auth=Blueprint('auth',__name__)

bd = getConecction()




@auth.route('/login', methods=['post'])
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



@auth.route('/cambiar-contraseña', methods=['post'])
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


@auth.route('/forgot', methods=['post'])
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