from app import app
from flask import jsonify, request
from models.modelosSimples import getPrograms, getTipoDocumento, getSedes, getMaterias, getSalon, getEstadoTutoria, getFacultades
from databases.conexion import getConecction
from models.horario import Horario
from models.horario_modelos import getTutoriaForId
from models import consultasHorario
from models.consultasHorario import consultasHorario
from models.modelosAdmin import ModelosAdmin

bd = getConecction()


@app.route('/salon',)
def salon():
    salon = getSalon()
    return jsonify(salon)


@app.route('/estadoTutoria')
def estadoTutoria():
    estado = getEstadoTutoria()
    return jsonify(estado)


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


@app.route('/facultades')
def facultades():
    facultades = getFacultades()
    print(facultades)
    return jsonify(facultades)


@app.route('/obtenerCapacidad', methods=['post'])
def obtenerCapacidad():

    data = request.json
    id_salon, id_capacidad, id_sede = Horario.obtenerSalon(data['salon'])
    print(id_salon, id_capacidad, id_sede)

    capacidad = Horario.obtenerCapacidad(id_capacidad)

    return jsonify({"data": capacidad})

    # if not logout:
    #     return jsonify({"message":"error"})

# @app.route('/renew-token', methods=['POST'])
# def renew_token():
#     data = request.get_json()
#     token = data.get('token')  # Token a renovar

#     if token:
#         new_token = Security.renew_token(token)
#         if new_token:
#             return jsonify({'new_token': new_token}), 200
#         else:
#             return jsonify({'message': 'Token renewal failed'}), 401
#     else:
#         return jsonify({'message': 'Token not provided'}), 400


@app.route('/buscarPrograma/<facultad>')
def buscarProgramas(facultad):
    modelo = ModelosAdmin(bd)
    id_facultad = modelo.obtenerIdFacultad(facultad)
    programas = modelo.buscarProgramas(id_facultad)
    print(programas)
    return jsonify({"data": programas}), 201


@app.route('/obtenerTutoria/<id_tutoria>', methods=['get'])
def obtenerTutoria(id_tutoria):
    tutoria = getTutoriaForId(id_tutoria)
    horario = consultasHorario.serializeTutoria(tutoria)
    return jsonify({"data": horario})
