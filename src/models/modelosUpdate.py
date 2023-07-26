import mysql.connector

from models.horario import Horario

class ModelosUpdate():


    def __init__ (self,bd:mysql.connector.connection.MySQLConnection):
        self.bd=bd
        self.cursor=bd.cursor()


    def obtenerIdsTabla(self,id_tutoria,data):
      
        sql=f"""SELECT
  (SELECT id_programa FROM programas WHERE programa = "{data['programa']}") AS id_programa,
  (SELECT id_sede FROM sedes WHERE sede = "{data['sede']}") AS id_sede,
  (SELECT id_salon FROM salones WHERE salon = "{data['salon']}") AS id_salon,
  (SELECT id_estado_tutoria FROM estados_tutorias WHERE estado_tutoria = "{data['estadoTutoria']}") AS id_estado_tutoria,
  (SELECT id_capacidad FROM capacidades WHERE capacidad = "{data['capacidad']}") AS id_capacidad,
  (SELECT id_materia FROM materias WHERE materia = "{data['materia']}") AS id_materia,
  (SELECT id_facultad FROM facultades WHERE facultad = "{data['facultad']}") AS id_facultad;


 """
        print(sql)
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        print('hi',data)
        return {
            "id_programa":data[0][0],
            "id_sede":data[0][1],
            "id_salon":data[0][2],
            "id_estado_tutoria":data[0][3],
            "id_capacidad":data[0][4],
            "id_materia":data[0][5],
            "id_facultad":data[0][6]
        }
    def actualizarTutoria(self,horario:Horario):
        
        sql=f"UPDATE horario_tutorias set id_programa='{horario.id_programa}',id_materia='{horario.id_materia}',id_sede='{horario.id_sede}',id_salon='{horario.id_salon}',id_estado_tutoria='{horario.id_estado_tutoria}',cupos='{horario.cupos}',tema='{horario.tema}',fecha='{horario.fecha}',hora_inicial='{horario.hora_inicio}',hora_final='{horario.hora_final}' WHERE id_tutoria={horario.id_tutoria}"
        print(sql)
        self.cursor.execute(sql)
        self.bd.commit()
        
    def obtenerCupos(self , id_tutoria):
        sql=f"select cupos from horario_tutorias where id_tutoria={id_tutoria}"
        self.cursor.execute(sql)
        cupos=self.cursor.fetchone()[0]
        return cupos
    def obtenerEstado(self,estado):
        sql=f"select id_estado_tutoria from estados_tutorias where estado_tutoria='{estado}'"
        self.cursor.execute(sql)
        cupos=self.cursor.fetchone()[0]
        return cupos