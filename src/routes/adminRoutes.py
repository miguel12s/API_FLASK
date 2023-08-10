from flask import Blueprint, jsonify
from flask import request
from models.modelosAdmin import ModelosAdmin
from databases.conexion import getConecction
from models.modelosUpdate import ModelosUpdate
admin=Blueprint("admin",__name__)
bd=getConecction()
modelo=ModelosAdmin(bd)
from models.horario import Horario



@admin.route('/agregarFacultad',methods=['post'])

def agregarFacultad():
    body=request.json
    modelo.agregarFacultad(body['facultad'])
    return jsonify("La facultad ha sido agregada con exito")
@admin.route('obtenerFacultades',methods=['get'])

def obtenerFacultades():
       data=modelo.obtenerFacultades()
       return jsonify({"data":data})

@admin.route('/actualizar',methods=['post'])

def actualizarFacultad():
    data=request.json
    
    try:
      modelo.actualizarFacultad(data)
    except:
      return jsonify({"error":"La facultad ya se encuentra registrada en el sistema"})
    return jsonify({"success":"La facultad ha sido actualizada"})

@admin.route('/getFacultadForId/<id_facultad>',methods=['get'])

def getFacultadForId(id_facultad):
      facultad=modelo.obtenerFacultadPorId(id_facultad)
      return jsonify({"data":facultad})


@admin.route('/setFacultad', methods=['POST'])

def setFacultad():
    data=request.json
    print(data)
    try:
        modelo.agregarFacultad(data['facultad'])
    except:
        return jsonify({"error":"La facultad ya se encuentra registrada en el sistema"})
    return jsonify({"data":"La facultad ha sido agregada con exito"})





@admin.route('/agregarPrograma',methods=['post'])

def agregarPrograma():
    body=request.json
    try:
      modelo.agregarPrograma(body['programa'])
    except:
        return jsonify({"error":"El programa ya se encuentra registrado en el sistema"})
    return jsonify("El programa ha sido agregado con exito")
@admin.route('obtenerProgramas',methods=['get'])

def obtenerProgramas():
       data=modelo.obtenerProgramas()
        
       

       return jsonify({"data":data})

@admin.route('/actualizarPrograma',methods=['post'])

def actualizarProgramas():
    data=request.json
    
    try:
      modelo.actualizarPrograma(data)
    except:
      return jsonify({"error":"El programa ya se encuentra registrado en el sistema"})
    return jsonify({"success":"El programa ha sido actualizado"})

@admin.route('/getProgramaForId/<id_programa>',methods=['get'])

def getProgramaForId(id_programa):
      programa=modelo.obtenerProgramaPorId(id_programa)
      return jsonify({"data":programa})


@admin.route('/setPrograma', methods=['POST'])

def setPrograma():
    data=request.json
    try:
      modelo.agregarPrograma(data['programa'])
    except:
        return jsonify({"error":"El programa ya se encuentra registrado en el sistema"})
        
        
    return jsonify({"data":" El programa ha sido agregado con exito"})








@admin.route('/agregarMateria',methods=['post'])

def agregarMateria():
    body=request.json
    try:
      modelo.agregarMateria(body['materia'])

    except:
      return jsonify({"error":"La materia ya se encuentra registrada en el sistema"})
    return jsonify({"data":"La materia ha sido agregada con exito"})
@admin.route('obtenerMaterias',methods=['get'])

def obtenerMaterias():
       data=modelo.obtenerMaterias()
       return jsonify({"data":data})

@admin.route('/actualizarMateria',methods=['post'])

def actualizarMateria():
    data=request.json
    
    try:
      modelo.actualizarMateria(data)
    except:
      return jsonify({"error":"La materia ya se encuentra registrada en el sistema"})
    return jsonify({"success":"La materia ha sido actualizada"})

@admin.route('/getMateriaForId/<id_materia>',methods=['get'])

def getMateriaForId(id_materia):
      materia=modelo.obtenerMateriaPorId(id_materia)
      return jsonify({"data":materia})



@admin.route('/getSedes')

def getSedes():
    sedes=modelo.getSedes()
    return jsonify({"data":sedes})

@admin.route('/getDataForIdSede/<id_sede>')

def getDataForIdSede(id_sede):
    sede=modelo.obtenerSedePorId(id_sede)
    return jsonify({"data":sede})

@admin.route('setSede',methods=['post'])
def setSede():
    body=request.json
    try:
      modelo.agregarSede(body['sede'])
    except:
        return jsonify({"error":"La sede ya se encuentra registrada en el sistema"})
    return jsonify({"data":"La sede ha sido agregada con exito"})

@admin.route('actualizarSede',methods=['post'])
def actualizarSede():
     data=request.json
     try:
      modelo.actualizarSede(data)
     except:
      return jsonify({"error":"La sede ya se encuentra registrada en el sistema"})
     return jsonify({"success":"La sede ha sido actualizada"})


@admin.route('getSalones',methods=['get'])


def getSalones():
    salones=modelo.getSalones()
    return jsonify({"data":salones})



@admin.route('/getSalonForId/<id_salon>',methods=['get'])

def getSalonForId(id_salon):
      salon=modelo.obtenerSalonPorId(id_salon)
      return jsonify({"data":salon})

@admin.route('/setSalon', methods=['POST'])

def setSalon():
    salon=request.json
    try:
      ids=modelo.obtenerIds(salon)
      print(ids)
      modelo.agregarSalon(ids,salon['salon'])
    except Exception as e:
        print(e)
        return jsonify({"error":"El salón ya se encuentra registrado en el sistema"})
    return jsonify({"data":"El salón ha sido agregado con exito"})

@admin.route('actualizarSalon',methods=['post'])


def actualizarSalon():
   body=request.json
   try:
      ids=modelo.obtenerIds(body)
      modelo.actualizarSalon(ids,body)
   except Exception as e:
      
      print(e)
      return jsonify({"error":"El salon ya se encuentra registrado en el sistema"})
   return jsonify({"success":"El salon ha sido actualizado"})

@admin.route('/getRoles')

def roles():
    roles=modelo.getRoles()
    return jsonify({"data":roles})



@admin.route('/getRolForId/<id_rol>')
def getRolForId(id_rol):
    roles=modelo.obtenerRolPorId(id_rol)
    return jsonify({"data":roles})
@admin.route('setRol',methods=['post'])


def setRol():
   roles=request.json
   try:
      modelo.setRol(roles)
   except:
        return jsonify({"error":"El rol ya se encuentra registrado en el sistema"})
   return jsonify({"data":"El rol ha sido agregado con exito"})





@admin.route('actualizarRol',methods=['post'])
def actualizarRol():
     data=request.json
     try:
      modelo.actualizarRol(data)
     except:
      return jsonify({"error":"EL rol ya se encuentra registrado en el sistema"})
     return jsonify({"success":"El rol ha sido actualizado"})





@admin.route('/getTipo')

def getTipo():
    tipo=modelo.getTipo()
    return jsonify({"data":tipo})



@admin.route('/getTipoForId/<id_tipo>')
def getTipoForId(id_tipo):
    tipos=modelo.obtenerTipoPorId(id_tipo)
    return jsonify({"data":tipos})
@admin.route('setTipo',methods=['post'])


def setTipo():
   tipos=request.json
   try:
      modelo.setTipo(tipos)
   except:
        return jsonify({"error":"El tipo de documento ya se encuentra registrado en el sistema"})
   return jsonify({"data":"El tipo de documento ha sido agregado con exito"})





@admin.route('actualizarTipo',methods=['post'])
def actualizarTipo():
     data=request.json
     try:
      modelo.actualizarTipo(data)
     except:
      return jsonify({"error":"El tipo de documento ya se encuentra registrado en el sistema"})
     return jsonify({"success":"El tipo de documento ha sido actualizado"})






@admin.route('/getEstado')

def getEstado():
    estado=modelo.getEstado()
    return jsonify({"data":estado})



@admin.route('/getEstadoForId/<id_estado>')
def getEstadoForId(id_estado):
    estado=modelo.obtenerEstadoPorId(id_estado)
    return jsonify({"data":estado})
@admin.route('setEstado',methods=['post'])


def setEstado():
   estados=request.json
   try:
      modelo.setEstado(estados)
   except:
        return jsonify({"error":"El estado de usuario ya se encuentra registrado en el sistema"})
   return jsonify({"data":"El estado ha sido agregado con exito"})





@admin.route('actualizarEstado',methods=['post'])
def actualizarEstado():
     data=request.json
     try:
      modelo.actualizarEstado(data)
     except Exception as e:
      print(e)
      return jsonify({"error":"El estado de usuario ya se encuentra registrado en el sistema"})
     return jsonify({"success":"El estado de usuario ha sido actualizado"})






@admin.route('/getEstadoTutoria')

def getEstadoTutoria():
    estadoTutoria=modelo.getEstadoTutoria()
    return jsonify({"data":estadoTutoria})



@admin.route('/getEstadoTutoriaForId/<id_estado_tutoria>')
def getEstadoTutoriaForId(id_estado_tutoria):
    estado=modelo.obtenerEstadoTutoriaPorId(id_estado_tutoria)
    return jsonify({"data":estado})
@admin.route('setEstadoTutoria',methods=['post'])


def setEstadoTutoria():
   estados=request.json
   try:
      modelo.setEstadoTutoria(estados)
   except:
        return jsonify({"error":"El estado de la tutoria ya se encuentra registrado en el sistema"})
   return jsonify({"data":"El estado de la tutoria ha sido agregado con exito"})





@admin.route('actualizarEstadoTutoria',methods=['post'])
def actualizarEstadoTutoria():
     data=request.json
     try:
      modelo.actualizarEstadoTutoria(data)
     except Exception as e:
      print(e)
      return jsonify({"error":"El estado de la tutoria  ya se encuentra registrado en el sistema"})
     return jsonify({"success":"El estado  de la tutoria ha sido actualizado"})





@admin.route('/getCapacidad')

def getCapacidad():
    capacidad=modelo.getCapacidad()
    return jsonify({"data":capacidad})



@admin.route('/getCapacidadForId/<id_capacidad>')
def getCapacidadForId(id_capacidad):
    capacidad=modelo.obtenerCapacidadPorId(id_capacidad)
    return jsonify({"data":capacidad})
@admin.route('setCapacidad',methods=['post'])


def setCapacidad():
   estados=request.json
   try:
      modelo.setCapacidad(estados)
   except:
        return jsonify({"error":"La capacidad ya se encuentra registrada en el sistema"})
   return jsonify({"data":"La capacidad ha sido agregada con exito"})





@admin.route('/actualizarCapacidad',methods=['post'])
def actualizarCapacidad():
     data=request.json
     try:
      modelo.actualizarCapacidad(data)
     except Exception as e:
      print(e)
      return jsonify({"error":"La capacidad ya se encuentra registrada en el sistema"})
     return jsonify({"success":"La capacidad ha sido actualizada"})

@admin.route('/obtenerHorarioDocente',methods=['get'])

def obtenerHorario():
   data=modelo.getHorario()

   return jsonify({"data":data})

@admin.route('/actualizarHorarioAdmin/<id_tutoria>',methods=['POST'])

def actualizarHorarioAdmin(id_tutoria):

    body=request.json
    print("body",body)
    ids=modelo.obtenerIdsTabla(body)
    print(ids)
    modelo.actualizarTutoria(body,ids)
    return jsonify({"data":"actualizado con exito"})


@admin.route('/getDocente')

def getDocente():
   docentes=modelo.getDocente()
   return jsonify({"data":docentes})

@admin.post('/crearHorario')

def crearHorario():
   body=request.json
   
   print(body)
   id_usuario=body['docente'].split('-')[1]

   existeFecha=Horario.verificarFecha(body['horaInicio'],body['horaFin'],body['fecha'],id_usuario)
   print(existeFecha)
   if(existeFecha==0):
    ids=modelo.obtenerIdsTabla(body)
    print(ids)
    modelo.crearHorario(body,ids)
    return jsonify({"message":"el horario ha sido añadido con exito"})
   else:
      return jsonify({"error":"ya existe un horario creado a esa misma hora y fecha"})


@admin.route('/obtenerHorarioTerminado',methods=['get'])

def obtenerHorarioTerminado():
   data=modelo.getHorarioFinished()

   return jsonify({"data":data})
@admin.route('/getEstudiantes',methods=['get'])

def getEstudiantes():
    estudiantes=modelo.getEstudiantes()
    return jsonify({"data":estudiantes})

@admin.route('/modificarEstadoUsuario',methods=['post'])

def modificarEstadoUsuario():
    body=request.json
    modeloUpdate=ModelosUpdate(bd)
    modeloUpdate.actualizarEstado(body)
    return jsonify({"success":"el estado ha sido actualizado"})

@admin.route('getEstudiante/<id_usuario>',methods=['get'])


def getEstudiante(id_usuario):
    estudiante=modelo.getEstudiante(id_usuario)
    print(estudiante)
    return jsonify({"data":estudiante})

@admin.post('actualizarEstudiante/<id_estudiante>')


def actualizarEstudiante(id_estudiante):
   estudiante=request.json
   id_estado=modelo.getEstadoForEstado(estudiante['estado'])
   modelo.actualizarUsuario(id_estudiante,id_estado,estudiante['correo'])
   modelo.actualizarEstudiante(id_estudiante,estudiante) 


   return jsonify({"success":"el estudiante ha sido actualizado"})
@admin.route('/getDocentesFull')

def getDocentes():
   docentes=modelo.getDocentess()
   print(docentes)
   return jsonify({"data":docentes})

## obtener un solo docente para el actualizar con su id_usuario

@admin.route('/getDocente/<id_usuario>')

def getDocenteFull(id_usuario):
   docente=modelo.getDocenteFull(id_usuario)
   return jsonify({"data":docente})

@admin.post('/actualizarDocente/<id_usuario>')

def actualizarDocente(id_usuario):
   docente=request.json
   id_estado=modelo.getEstadoForEstado(docente['estado'])
   modelo.actualizarUsuario(id_usuario,id_estado,docente['correo'])
   modelo.actualizarDocente(id_usuario,docente) 
   return jsonify({"message":"el docente ha sido actualizado"})

