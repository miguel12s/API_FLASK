
from databases.conexion import getConecction
from datetime import datetime

class Horario:
    id_tutoria:int
    id_facultad:int
    id_programa:int
    id_materia:int
    id_sede:int
    id_salon:int
    id_usuario:int
    id_estado_tutoria:int
    cupos:int
    tema:str
    fecha:str
    hora_inicio:str
    hora_final:str
    fecha_generacion_tutoria:str
    def __init__(self,id_tutoria,id_facultad,id_programa,id_materia,id_sede,id_salon,id_usuario,id_estado_tutoria,cupos,tema,fecha,hora_inicio,hora_final,fecha_generacion_tutoria) -> None:
        self.id_tutoria=id_tutoria
        self.id_facultad=id_facultad
        self.id_programa=id_programa
        self.id_materia=id_materia
        self.id_sede=id_sede
        self.id_salon=id_salon
        self.id_usuario=id_usuario
        self.id_estado_tutoria=id_estado_tutoria
        self.cupos=cupos
        self.tema=tema
        self.fecha=fecha
        self.hora_final=hora_final
        self.fecha_generacion_tutoria=fecha_generacion_tutoria
        self.hora_inicio=hora_inicio
    @classmethod
    def agregarMateria(self,materia):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f" select id_materia from materias where materia='{materia}'"
        cursor.execute(sql)

        id_materia=cursor.fetchone()[0]
        print('el id de la materia es ',id_materia)
        return id_materia
        
    @classmethod
    def agregarSede(self,sede):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"select id_sede from sedes where sede='{sede}'"
        cursor.execute(sql)
        return cursor.fetchone()[0]


    
            
    @classmethod
    def agregarSalon(self,salon,id_capacidad):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"insert into salones (id_salon,id_capacidad,salon) values('{0}','{id_capacidad}','{salon}')"
        cursor.execute(sql)
        bd.commit()
        return cursor.getlastrowid()
    @classmethod  
    def agregarCapacidad(self,capacidad):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"insert into capacidades (id_capacidad,capacidad) values('{0}','{capacidad}')"
        cursor.execute(sql)

        bd.commit()
        return cursor.getlastrowid()
       
    @classmethod
    def agregarHorario(self,horario):
        bd=getConecction()
        cursor=bd.cursor()
        fecha=datetime.now()
        print('id_programa',horario.id_programa)
        sql=f"insert into horario_tutorias (id_tutoria, id_facultad, id_programa, id_materia, id_sede, id_salon, id_usuario, id_estado_tutoria, cupos, tema, fecha, hora_inicial, hora_final, fecha_generacion_tutoria) VALUES ('{0}','{horario.id_facultad}','{horario.id_programa}','{horario.id_materia}','{horario.id_sede}','{horario.id_salon}','{horario.id_usuario}','{horario.id_estado_tutoria}','{horario.cupos}','{horario.tema}','{horario.fecha}','{horario.hora_inicio}','{horario.hora_final}','{fecha}')" 
        cursor.execute(sql)
        bd.commit()

    @classmethod
    def getLittleDataForTeacher(self,id_teacher):
       bd=getConecction()
       cursor=bd.cursor()
       sql=f"select nombres,apellidos,facultad from docentes where id_usuario='{id_teacher}'"
       cursor.execute(sql)
       data=cursor.fetchone()
       
       
       return data
    @classmethod
    def serialize(self,data):
        dataNombres=f"{data[0]  } {data[1]}"
        return {
            'nombre':dataNombres,
            'facultad':data[2]
        }
    
    @classmethod
    def buscarPrograma(self,programa):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"select id_programa from programas where programa='{programa}' "
        cursor.execute(sql)
        id_programa=cursor.fetchone()[0]
        return id_programa
    @classmethod
    def buscarFacultad(self,facultad):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"select id_facultad from facultades where facultad='{facultad}' "
        cursor.execute(sql)
        id_programa=cursor.fetchone()[0]
        return id_programa
    @classmethod

    def obtenerSalon(self,salon):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"select id_salon,id_capacidad from salones where salon='{salon}' "
        cursor.execute(sql)
        data=cursor.fetchall()
        return data[0][0],data[0][1]

    @classmethod
    def obtenerCapacidad(self,id_salon):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"select capacidades.capacidad from capacidades join salones on capacidades.id_capacidad=salones.id_capacidad WHERE capacidades.id_capacidad={id_salon}"
        cursor.execute(sql)
        return cursor.fetchone()[0]

       
    

              