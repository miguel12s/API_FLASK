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
    modelo.agregarPrograma(body['programa'])
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
    print(data)
   
    modelo.agregarPrograma(data['programa'])
   
        
        
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






