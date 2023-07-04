from flask import Flask, jsonify, request
from flask_cors import CORS
from models.modelosSimples import getPrograms, getTipoDocumento
from models.estudiante import Estudiante
from models.user import User
from models.modelos import getPasswordHash,searchUserForRol,getPasswordForId,updatePassword
from utils.Security import Security
from flask_login import LoginManager,login_required,login_user,logout_user

app = Flask(__name__)
CORS(app, origins='http://localhost:4200')

app.secret_key="secret_key"
login_manager=LoginManager()
login_manager.init_app(app)


@app.route('/programas')
def programas():
    programas = getPrograms()
    return jsonify(programas)


@app.route('/tipo-documento')
def tipoDocumento():
    tipoDocumento = getTipoDocumento()
    return jsonify(tipoDocumento)


@app.route('/registro', methods=['post'])
def registro():
    response = {}
    status = 0
    try:
        data: Estudiante = request.json
        if not data:
            response = {'message': 'no hay datos en la request'}
            status = 400
            return jsonify(response, status, data)
        usuario = User(None,'1', '1', data['correo'], data['contraseña'])
        id = User.save(usuario)
        estudiante = Estudiante(id, data['nombre'], data['apellido'], data['tipoDocumento'],
                                data['numeroDocumento'], data['numeroTelefono'], data['programa'], data['facultad'], data['correo'])
        Estudiante.save(estudiante)
        status = 200
        response = {'message': "solicitud procesada"}
        return jsonify(response)
    except Exception as e:
        return jsonify({'message': "error"})

@login_manager.user_loader
def load_user(user_id):
  
    return User.get(user_id)

@app.route('/login',methods=['post','get'])
def login():
    

    data=request.json
    if not data:
        return jsonify({'message':"no hay datos en la request"})
     
    passwordHashed=getPasswordHash(data['correo'])
    user = User.get_by_email(data['correo'])
    
    if(passwordHashed!=None):
         id_usuario, id_rol = searchUserForRol(passwordHashed,data)
         if(id_usuario!=False):
             if (id_rol != None):
                 print("el correo es",user.correo)
                 login_user(user)
                 token = Security.generateToken(id_usuario)
                 message=({"success": True, 'token': token,"rol":id_rol,"usuario":id_usuario})
             else:
                 message=({"success":False})
         else:
          message=({"success":False})
         return jsonify(message)
    else:
         return jsonify(message)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Cierre de sesión exitoso'})



@app.route('/protected')
@login_required
def protected():
    return jsonify({'message':"ruta protegida"})


@app.route('/perfil/<id>')


def perfil(id):
    print(id)
  
    estudiante=Estudiante.get(id)
    return jsonify(estudiante.serialize())
    
@app.route('/cambiar-contraseña/<id>',methods=['post'])


def cambiar_contraseña(id):
    response=request.json
    contraseña=response['contraseña'],
    nuevaContraseña=response['nuevaContraseña']
    hashedPassword=getPasswordForId(id)
    if(User.checkPassword(hashedPassword,contraseña[0])):
        updatePassword(id,User.generatePassword(nuevaContraseña))
        
        return jsonify({"message":"la contraseña ha sido cambiada"})              
    return jsonify({"message":"la contraseña no ha sido cambiada"})
if __name__ == '__main__':
    app.run(debug=True)
