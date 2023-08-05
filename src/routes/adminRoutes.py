from flask import Blueprint, jsonify
from flask import request
from models.modelosAdmin import ModelosAdmin
from databases.conexion import getConecction
from models.modelosUpdate import ModelosUpdate
admin=Blueprint("admin",__name__)
bd=getConecction()
modelo=ModelosAdmin(bd)



@admin.route('/agregarFacultad',methods=['post'])

def agregarFacultad():
    body=request.json
    modelo.agregarFacultad(body['facultad'])
    return jsonify("la facultad ha sido agregada con exito")
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
      return jsonify({"error":"el nombre de la tabla ya se encuentra registrado en el programa"})
    return jsonify({"success":"la facultad ha sido actualizada"})

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
        return jsonify({"error":"la facultad ya se encuentra registrada en el sistema"})
    return jsonify({"data":" la facultad ha sido agregado con exito"})





@admin.route('/agregarPrograma',methods=['post'])

def agregarPrograma():
    body=request.json
    try:
      modelo.agregarPrograma(body['programa'])
    except:
        return jsonify({"error":"El programa que desea insertar se encuenta registrado en el programa"})
    return jsonify("el programa ha sido agregada con exito")
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
      return jsonify({"error":"el nombre de la tabla ya se encuentra registrado en el programa"})
    return jsonify({"success":"El programa ha sido actualizada"})

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
        return jsonify({"error":"El programa que desea insertar se encuenta registrado en el programa"})
        
        
    return jsonify({"data":" El programa ha sido agregado con exito"})








@admin.route('/agregarMateria',methods=['post'])

def agregarMateria():
    body=request.json
    try:
      modelo.agregarMateria(body['materia'])

    except:
      return jsonify({"error":"el nombre de la tabla ya se encuentra registrado en la materia"})
    return jsonify({"data":"la materia ha sido agregada con exito"})
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
      return jsonify({"error":"el nombre de la tabla ya se encuentra registrado en el programa"})
    return jsonify({"success":"El programa ha sido actualizada"})

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
        return jsonify({"error":"la sede ya existe en el programa"})
    return jsonify({"data":"la sede ha sido agregada con exito"})

@admin.route('actualizarSede',methods=['post'])
def actualizarSede():
     data=request.json
     try:
      modelo.actualizarSede(data)
     except:
      return jsonify({"error":"el nombre de la sede ya se encuentra registrado en el programa"})
     return jsonify({"success":"la sede ha sido actualizada"})


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
        return jsonify({"error":"la sede ya existe en el programa"})
    return jsonify({"data":"la sede ha sido agregada con exito"})

@admin.route('actualizarSalon',methods=['post'])


def actualizarSalon():
   body=request.json
   try:
      ids=modelo.obtenerIds(body)
      modelo.actualizarSalon(ids,body)
   except Exception as e:
      
      print(e)
      return jsonify({"error":"el salon ya existe en el sistema"})
   return jsonify({"success":"el salon ha sido actualizado"})

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
        return jsonify({"error":"el rol ya existe en el programa"})
   return jsonify({"data":"el rol ha sido agregada con exito"})





@admin.route('actualizarRol',methods=['post'])
def actualizarRol():
     data=request.json
     try:
      modelo.actualizarRol(data)
     except:
      return jsonify({"error":"el nombre del rol  ya se encuentra registrado en el programa"})
     return jsonify({"success":"el rol ha sido actualizada"})





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
        return jsonify({"error":"el tipo de documento ya existe en el programa"})
   return jsonify({"data":"el tipo de documento ha sido agregada con exito"})





@admin.route('actualizarTipo',methods=['post'])
def actualizarTipo():
     data=request.json
     try:
      modelo.actualizarTipo(data)
     except:
      return jsonify({"error":"el tipo de documento ya se encuentra registrado en el programa"})
     return jsonify({"success":"el tipo de documento ha sido actualizada"})






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
        return jsonify({"error":"el estado ya existe en el programa"})
   return jsonify({"data":"el estado ha sido agregado con exito"})





@admin.route('actualizarEstado',methods=['post'])
def actualizarEstado():
     data=request.json
     try:
      modelo.actualizarEstado(data)
     except Exception as e:
      print(e)
      return jsonify({"error":"el estado ya se encuentra registrado en el programa"})
     return jsonify({"success":"el estado ha sido actualizada"})






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
        return jsonify({"error":"el estado de la tutoria ya existe en el programa"})
   return jsonify({"data":"el estado de la tutoria ha sido agregado con exito"})





@admin.route('actualizarEstadoTutoria',methods=['post'])
def actualizarEstadoTutoria():
     data=request.json
     try:
      modelo.actualizarEstadoTutoria(data)
     except Exception as e:
      print(e)
      return jsonify({"error":"el estado de la tutoria  ya se encuentra registrado en el programa"})
     return jsonify({"success":"el estado  de la tutoria ha sido actualizada"})





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
        return jsonify({"error":"el estado de la tutoria ya existe en el programa"})
   return jsonify({"data":"el estado de la tutoria ha sido agregado con exito"})





@admin.route('/actualizarCapacidad',methods=['post'])
def actualizarCapacidad():
     data=request.json
     try:
      modelo.actualizarCapacidad(data)
     except Exception as e:
      print(e)
      return jsonify({"error":"el estado de la tutoria  ya se encuentra registrado en el programa"})
     return jsonify({"success":"el estado  de la tutoria ha sido actualizada"})

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


@admin.route('/getDocentes')

def getDocente():
   docentes=modelo.getDocente()
   return jsonify({"data":docentes})

@admin.post('/crearHorario')

def crearHorario():
   body=request.json
   
   print(body)
   ids=modelo.obtenerIdsTabla(body)
   print(ids)
   modelo.crearHorario(body,ids)
   return jsonify({"message":"el horario ha sido añadido con exito"})


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
   modelo.actualizarUsuario
   id_estado=modelo.getEstadoForEstado(estudiante['estado'])
   modelo.actualizarUsuario(id_estudiante,id_estado,estudiante['correo'])
   modelo.actualizarEstudiante(id_estudiante,estudiante) 


   return jsonify({"success":"el estudiante ha sido actualizado"})
