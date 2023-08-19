from flask import Blueprint,request,jsonify
from models.estudiante import Estudiante
from databases.conexion import getConecction
from models.horario_modelos import cancelarTutorias
from models.horario_modelos import actualizarCupos, obtenerCupos
from models.horario_modelos import mostrarTutoriasPendientesEstudiante
from models.horario import Horario
from models.horario_modelos import agendarTutoria, verificarListaDeEstudiantes
from models.horario_modelos import mostrarHorarioss
from models import TutoriasPendientes
from models.modelosSimples import existEmail, existNumeroDocumento
from models.user import User
from utils.Security import Security

estudiante=Blueprint("estudiante",__name__)
bd=getConecction()



@estudiante.route('/registro', methods=['post'])
def registro():
    response = {}
    status = 0
    try:
        data: Estudiante = request.json
        if not data:
            response = {'message': 'no hay datos en la request'}
            status = 400
            return jsonify(response, status, data)

        existemail = existEmail(data['correo'])
        existeNumeroDocumento = existNumeroDocumento(data['numeroDocumento'])

        if (existemail != 1 and existeNumeroDocumento != 1):

            usuario = User(None, '1', '1', data['correo'], data['contraseña'])
            id = User.save(usuario)

            estudiante = Estudiante(id, data['nombre'], data['apellido'], data['tipoDocumento'],
                                    data['numeroDocumento'], data['numeroTelefono'], data['facultad'], data['programa'], data['correo'], None)
            exist = Estudiante.save(estudiante)
            print(exist)

            status = 200
            response = {'message': "estudiante agregado"}
            return jsonify(response)
        if (existeNumeroDocumento == 1):
            return jsonify({"errorIdentificacion": "el numero de documento se encuentra registrado en el programa"})
        elif (existemail == 1):
            return jsonify({"error": "el correo se encuentra en el sistema"})
    except Exception as e:
        print(e)
        return jsonify({'message': "error"})



@estudiante.route('/perfil',methods=['get'])

def perfil():
    
    headers=request.headers
    payload=Security.verify_token(headers)
    print(payload)
    id_usuario=payload['id_usuario']
    
    
    estudiante=Estudiante.get(id_usuario)
    print('estudiante perfil',estudiante.serialize())
    return jsonify(estudiante.serialize())
@estudiante.route('/cancelarTutoria',methods=['post'])


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





@estudiante.get('/mostrarTutoriasEstudiante')

def mostrarTutoriasEstudiante():
    headers=request.headers
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']
    tutoriasPendientesEstudiante=mostrarTutoriasPendientesEstudiante(id_usuario)
    tutoriasJson=Horario.serializeHorario(tutoriasPendientesEstudiante)
    print(tutoriasJson)
   
    return jsonify({"data":tutoriasJson})

@estudiante.post('/agendar')

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
            agendarTutoria(id_usuario, id_tutoria, 1)
            cupos-=1
            actualizarCupos(cupos
                ,id_tutoria)
            return jsonify({"message": "agendamiento creado con exito"})
        else:
            return jsonify({"errorCupos":"los cupos estan completos :("})
  
    return jsonify({"error": "Ya ha agendado esta tutoria"})


@estudiante.route('/mostrarHorarios')

def mostrarHorarios():
    headers=request.headers
    payload=Security.verify_token(headers)
    horario=mostrarHorarioss()
    horarioTutorias=Horario.serializeHorario(horario)
    return jsonify({"data":horarioTutorias})


@estudiante.route('/obtenerTutoriasPendientes',methods=['get'])

def obtenerTutoriasPendientes():
    headers=request.headers
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']
    tutorias=TutoriasPendientes(bd)
    data=tutorias.TutoriasPendientes(id_usuario)
    dataJson=Horario.serializeHorario(data)
    print(dataJson)
    return jsonify({"data":dataJson})




