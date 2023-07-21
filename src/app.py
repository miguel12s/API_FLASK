import os
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, request,make_response,send_from_directory
from flask_cors import CORS
from models.modelosSimples import getPrograms, getTipoDocumento,getSedes,getMaterias,getSalon
from models.estudiante import Estudiante
from models.user import User
from models.modelos import getPasswordHash,searchUserForRol,getPasswordForId,updatePassword,getIdRol,getHorarioForId
from models.horario import Horario
from models.horario_modelos import mostrarHorarioss,agendarTutoria,actualizarCupos,verificarListaDeEstudiantes,mostrarTutoriasPendientesEstudiante,obtenerCupos,cancelarTutorias
from models.docente import Docente
from models import consultasHorario
from models.consultasHorario import consultasHorario
from utils.Security import Security
import jwt
import json


app = Flask(__name__)

UPLOAD_FOLDER ='src/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

CORS(app, origins='http://localhost:4200',supports_credentials=True)
app.secret_key="secret_key"

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    print("hola")
    return '.' in filename and filename.rsplit('.', 1)[1].lower()

@app.route("/upload",methods=["POST"])
def upload():
    
    verify = request.headers
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
    rol=getIdRol(id_usuario)
    print(rol)
    if(rol==1):
        Estudiante.updateImage( filename, id_usuario)
        print(image_path)
        estudiante= Estudiante.get(id_usuario)
        response = jsonify({'message': 'Archivo subido correctamente', 'imgPath': image_path,'datos':estudiante.serialize()})
        
    elif(rol==2):
        Docente.updateImage(filename,id_usuario)
        docente=Docente.get(id_usuario)
        response = jsonify({'message': 'Archivo subido correctamente', 'imgPath': image_path,'datos':docente.serialize()})
    
  

    return response,200
   
@app.route('/display/<filename>')

def display(filename):
   
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/salon',)
def salon():
    salon = getSalon()
    return jsonify(salon)

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
                                data['numeroDocumento'], data['numeroTelefono'], data['programa'], data['facultad'], data['correo'],None)
        Estudiante.save(estudiante)
        status = 200
        response = {'message': "solicitud procesada"}
        return jsonify(response)
    except Exception as e:
        print(e)
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
    print('estudiante perfil',estudiante.serialize())
    return jsonify(estudiante.serialize())

@app.route('/perfil-docente',methods=['get'])

def perfilDocente():
    
    headers=request.headers
    payload=Security.verify_token(headers)
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
        print(usuario)
        id = User.save(usuario)
        foto="https://acsilat.org/images/2020/05/06/teacher.png"
        docente = Docente(id, data['nombre'], data['apellido'], data['tipoDocumento'],
                                data['numeroDocumento'], data['numeroTelefono'],  data['facultad'], data['correo'],foto)
        Docente.save(docente)
        
        status = 200
        response = {'message': "solicitud procesada"}
        return jsonify(response)
    
@app.route('/agregarHorario',methods=['post'])

def agregarHorario():
    horario=request.json
    print(horario)
    headers=request.headers
    print(horario['facultad'])
    payload=Security.verify_token(headers)
    
    id_facultad=Horario.buscarFacultad(horario['facultad'])
    id_programa=Horario.buscarPrograma(horario['programa'])
    id_materia=Horario.agregarMateria(horario['materia'])
    id_capacidad=Horario.agregarCapacidad(horario['capacidad'])
    id_salon=Horario.agregarSalon(horario['salon'],id_capacidad)
    id_sede=Horario.agregarSede(horario['sede'])
    id_usuario=payload['id_usuario']
    horario=Horario(0,id_facultad,id_programa,id_materia,id_sede,id_salon,id_usuario,1,horario['capacidad'],horario['tema'],horario['fecha'],horario['horaInicio'],horario['horaFin'],None)
    Horario.agregarHorario(horario)
    return jsonify({"horario":"horario creado"})
    
@app.route('/horario')

def horario():
    headers=request.headers
    payload=Security.verify_token(headers)
    user_id=payload['id_usuario']
    datos= Horario.getLittleDataForTeacher(user_id)
    dataModificada=Horario.serialize(datos)
    return jsonify({"data":dataModificada})


@app.route('/obtenerCapacidad',methods=['post'])

def obtenerCapacidad():
    
    data=request.json
    headers=request.headers
    print(data)
    payload=Security.verify_token(headers)
    id_salon,id_capacidad=Horario.obtenerSalon(data['salon'])
    print(id_salon,id_capacidad)
    
    capacidad=Horario.obtenerCapacidad(id_capacidad)
   
    return jsonify({"capacidad":capacidad})

@app.route('/mostrarHorario')

def mostrarHorario():
    headers=request.headers
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']
    
    ids=consultasHorario.obtenerIds(id_usuario)
    data=consultasHorario.mostrarHorario(ids)
    tutorias=consultasHorario.serialize(data)
   
    
    return jsonify({"data":tutorias})

@app.route('/mostrarHorarios')

def mostrarHorarios():
    headers=request.headers
    payload=Security.verify_token(headers)
    horario=mostrarHorarioss()
    horarioTutorias=Horario.serializeHorario(horario)
    print(horarioTutorias)
    return jsonify({"data":horarioTutorias})

@app.route('/mostrarHorariosId/<id>')

def mostrarHorariosId(id):
    print(id)
    headers=request.headers
    payload=Security.verify_token(headers)
    horario=getHorarioForId(id)
    horarioTutorias=consultasHorario.serializeId(horario)
    print(horarioTutorias)
    return jsonify({"data":horarioTutorias})

@app.route('/agendar',methods=['post'])

def agendar():
    headers=request.headers
    data=request.json
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']
   
    id_tutoria=data['id_tutoria']
    id_estado_tutoria=data['id_estado_tutoria']
    cupos=obtenerCupos(id_tutoria)
    verificar=verificarListaDeEstudiantes(id_usuario)
   
    tutoria_ya_agendada=any( tutoria == id_tutoria for tutoria in verificar)
    
    if not tutoria_ya_agendada:
        if cupos!=0:
            agendarTutoria(id_usuario, id_tutoria, id_estado_tutoria)
            cupos-=1
            actualizarCupos(cupos
                ,id_tutoria)
            return jsonify({"message": "agendamiento creado con exito"})
        else:
            return jsonify({"errorCupos":"los cupos estan completos :("})
  
    return jsonify({"error": "Ya ha agendado esta tutoria"})
    
@app.route('/mostrarTutoriasEstudiante',methods=['get'])

def mostrarTutoriasEstudiante():
    headers=request.headers
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']
    tutoriasPendientesEstudiante=mostrarTutoriasPendientesEstudiante(id_usuario)
    tutoriasJson=Horario.serializeHorario(tutoriasPendientesEstudiante)
    
    return jsonify({"data":tutoriasJson})

@app.route('/cancelarTutoria',methods=['post'])


def cancelarTutoria():
    headers=request.headers
    data=request.json
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']
    id_tutoria=data
    cancelarTutorias(id_tutoria,id_usuario)
    cupos=obtenerCupos(id_tutoria)
    cupos+=1
    actualizarCupos(cupos,id_tutoria)
    return jsonify({"data":"la tutoria ha sido cancelada"})




if __name__ == '__main__':
    app.run(debug=True,)
