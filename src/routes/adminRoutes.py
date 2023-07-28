from flask import Blueprint, jsonify
from flask import request
from models.modelosAdmin import ModelosAdmin
from databases.conexion import getConecction
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


@admin.route('getSalones')


def getSalones():
    salones=modelo.getSalones()
    print(salones)
    return jsonify({"data":salones})



@admin.route('/getSalonForId/<id_salon>',methods=['get'])

def getSalonForId(id_salon):
      salon=modelo.obtenerSalonPorId(id_salon)
      return jsonify({"data":salon})

