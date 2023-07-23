import mysql.connector

from models.horario import Horario

class ModelosUpdate():


    def __init__ (self,bd:mysql.connector.connection.MySQLConnection):
        self.bd=bd
        self.cursor=bd.cursor()


    def obtenerIdsTabla(self,id_tutoria):
      
        sql=f"""SELECT h.id_programa,h.id_sede,h.id_salon,h.id_estado_tutoria,c.id_capacidad,m.id_materia,f.id_facultad   from horario_tutorias h 
inner join programas p  on  h.id_programa=p.id_programa
inner join sedes s on h.id_sede=s.id_sede
inner join salones sa on h.id_salon=sa.id_salon
inner join materias m on h.id_materia=m.id_materia
inner join facultades f on h.id_facultad=f.id_facultad
inner join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria
inner join capacidades c on sa.id_capacidad=c.id_capacidad


where h.id_tutoria='{id_tutoria}'"""
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        print(data)
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
        self.cursor.execute(sql)
        self.bd.commit()
        print('actualizacion exitosa')
        
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