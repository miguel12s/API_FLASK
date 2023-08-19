from flask import Blueprint,request,jsonify
from models.TutoriasPendientes import TutoriasPendientes
from models.horario import Horario
from models.consultasHorario import consultasHorario
from utils.Security import Security
from models.docente import Docente
docente=Blueprint('docente',__name__)

@docente.route('/perfil-docente',methods=['get'])

def perfilDocente():
    
    headers=request.headers
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']    
    estudiante=Docente.get(id_usuario)
    return jsonify(estudiante.serialize())



@docente.route('/listado/<id_tutoria>')



def listado(id_tutoria):
    listado= TutoriasPendientes.listadoEstudiantes(id_tutoria) 
    return jsonify({"estudiante":listado})


@docente.delete('/eliminarTutoria/<id_tutoria>')

def eliminarTutoria(id_tutoria):
    try:
        
        Horario.eliminarListado(id_tutoria)
        Horario.eliminarHorario(id_tutoria)
        return jsonify({"success","el horario ha sido eliminado"},201)
    except Exception as e:
        print(e)
        return jsonify({"error":"el horario no se encuentra en el sistema"},404)


@docente.post('/agregarHorario')

def agregarHorario():
    horario=request.json
    headers=request.headers
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']
    existeFecha=Horario.verificarFecha(horario['horaInicio'],horario['horaFin'],horario['fecha'],id_usuario)
    print(existeFecha)
    if(existeFecha==0):
        id_facultad=Horario.buscarFacultad(horario['facultad'])
        id_programa=Horario.buscarPrograma(horario['programa'])
        id_materia=Horario.agregarMateria(horario['materia'])
        id_capacidad=Horario.agregarCapacidad(horario['capacidad'])
        id_salon=Horario.agregarSalon(horario['salon'],id_capacidad)
        id_sede=Horario.agregarSede(horario['sede'])
        horario=Horario(0,id_facultad,id_programa,id_materia,id_sede,id_salon,id_usuario,1,horario['capacidad'],horario['tema'],horario['fecha'],horario['horaInicio'],horario['horaFin'],None)
        Horario.agregarHorario(horario) 
        return jsonify({"horario":"horario creado"})
    else:
        return jsonify({"error":"ya existe un horario creado a esa misma hora y fecha"})
    

@docente.get('/mostrarHorarioEstado')

def mostrarHorarioEstado():
    headers=request.headers
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']
    
    ids=consultasHorario.obtenerIds(id_usuario)
    data=consultasHorario.mostrarHorarioEstado(ids)
    print("tutorias",data)
    tutorias=consultasHorario.serialize(data)
   
    
    return jsonify({"data":tutorias})

@docente.get('/horario')

def horario():
    headers=request.headers
    payload=Security.verify_token(headers)
    user_id=payload['id_usuario']
    datos= Horario.getLittleDataForTeacher(user_id)
    dataModificada=Horario.serialize(datos)
    return jsonify({"data":dataModificada})

@docente.get('/mostrarHorario')

def mostrarHorario():
    headers=request.headers
    payload=Security.verify_token(headers)
    id_usuario=payload['id_usuario']
    ids=consultasHorario.obtenerIds(id_usuario)
    data=consultasHorario.mostrarHorario(ids)
    tutorias=consultasHorario.serialize(data)
   
    
    return jsonify({"data":tutorias})
