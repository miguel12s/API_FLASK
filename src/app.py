from flask import Flask, jsonify, request,session
from flask_cors import CORS
from models.modelosSimples import getPrograms, getTipoDocumento
from models.estudiante import Estudiante
from models.user import User
from models.modelos import getPasswordHash,searchUserForRol,getPasswordForId,updatePassword
from models.docente import Docente
from utils.Security import Security

app = Flask(__name__)
CORS(app, origins='http://localhost:4200',supports_credentials=True)

app.secret_key="secret_key"


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



@app.route('/login',methods=['post'])
def login():
    
    message={}
    data=request.json
    if not data:
        return jsonify({'message':"no hay datos en la request"})
     
    passwordHashed=getPasswordHash(data['correo'])
    
    if(passwordHashed!=None):
         id_usuario, id_rol = searchUserForRol(passwordHashed,data)
         if(id_usuario!=False):
             print(id_usuario)
             if (id_rol != None):
            
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

def logout():
    return jsonify({'message': 'Cierre de sesión exitoso'})



@app.route('/protected')

def protected():
    return jsonify({'message':"ruta protegida"})


@app.route('/perfil',methods=['get'])

def perfil():
    
    headers=request.headers
    payload=Security.verify_token(headers)
    print(payload)
    id_usuario=payload['id_usuario']
    
    
    estudiante=Estudiante.get(id_usuario)
    return jsonify(estudiante.serialize())

@app.route('/perfil-docente',methods=['get'])

def perfilDocente():
    
    headers=request.headers
    payload=Security.verify_token(headers)
    print(payload)
    id_usuario=payload['id_usuario']
    
    
    estudiante=Docente.get(id_usuario)
    return jsonify(estudiante.serialize())
    
@app.route('/cambiar-contraseña',methods=['post'])


def cambiar_contraseña():
    response=request.json
    headers=request.headers
    payload=Security.verify_token(headers)
    id_usuario=payload.get('id_usuario')
    contraseña=response['contraseña'],
    nuevaContraseña=response['nuevaContraseña']
    hashedPassword=getPasswordForId(id_usuario)
    if(User.checkPassword(hashedPassword,contraseña[0])):
        newPassword=User.generatePassword(nuevaContraseña)
        updatePassword(id_usuario,newPassword)
        
        return jsonify({"message":"la contraseña ha sido cambiada"})              
    return jsonify({"message":"la contraseña no ha sido cambiada"})


@app.route('/agregar-docente',methods=['POST'])

def agregarDocente():
    
        data: Docente = request.json
        if not data:
            response = {'message': 'no hay datos en la request'}
            status = 400
            return jsonify(response, status, data)
        
        usuario = User(None,'2', '1', data['correo'], data['contraseña'])
        id = User.save(usuario)

        docente = Docente(id, data['nombre'], data['apellido'], data['tipoDocumento'],
                                data['numeroDocumento'], data['numeroTelefono'],  data['facultad'], data['correo'])
        Docente.save(docente)
        
        status = 200
        response = {'message': "solicitud procesada"}
        return jsonify(response)
    










if __name__ == '__main__':
    app.run(debug=True)
