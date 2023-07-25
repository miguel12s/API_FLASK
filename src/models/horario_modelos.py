from databases.conexion import getConecction
from models.horario import Horario


def mostrarHorarioss():
    bd=getConecction()
    cursor=bd.cursor()
    sql="select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,h.id_tutoria,f.facultad,p.programa,m.materia,s.sede,et.estado_tutoria,doc.nombres,doc.apellidos,sal.salon,capa.capacidad,et.id_estado_tutoria from horario_tutorias h join facultades f on h.id_facultad=f.id_facultad join programas p on h.id_programa=p.id_programa join materias m on h.id_materia=m.id_materia join sedes s on h.id_sede=s.id_sede join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria join docentes doc on h.id_usuario=doc.id_usuario join salones sal on h.id_salon=sal.id_salon join capacidades capa on h.id_salon=capa.id_capacidad where h.cupos!=0 and h.id_estado_tutoria=1"
    cursor.execute(sql)
    horarios=cursor.fetchall()
    return horarios

def agendarTutoria(id_usuario,id_tutoria,id_estado_tutoria):
    bd=getConecction()
    cursor=bd.cursor()
    sql=f"INSERT INTO lista_estudiantes(id_tutoria, id_usuario, id_estado_tutoria) VALUES ('{id_tutoria}','{id_usuario}',{id_estado_tutoria})"
    cursor.execute(sql)
    bd.commit()

def actualizarCupos(cupos,id_tutoria):
    
    bd=getConecction()
    cursor=bd.cursor()
    
    sql=f"update horario_tutorias set cupos={cupos} where id_tutoria={id_tutoria} "
    cursor.execute(sql)
    bd.commit()

def verificarListaDeEstudiantes(id_usuario):
    
    bd=getConecction()
    cursor=bd.cursor()
    try:
        sql=f"select id_tutoria from lista_estudiantes where id_usuario={id_usuario}"
        cursor.execute(sql)
        results=cursor.fetchall()
        
        if not results:
            return []
        else:
            id_tutorias=[result[0] for result in results]
            return id_tutorias
    except :
        print("error")
        return None
def mostrarTutoriasPendientesEstudiante(id_usuario):
    bd=getConecction()
    cursor=bd.cursor()
    try:
            sql=f"""
select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,le.id_tutoria,f.facultad ,p.programa,m.materia,se.sede,et.estado_tutoria,d.nombres,d.apellidos,s.salon,c.capacidad , s.salon,c.capacidad ,d.nombres,d.apellidos,et.id_estado_tutoria from lista_estudiantes le inner join horario_tutorias h on h.id_tutoria=le.id_tutoria inner join estados_tutorias et on le.id_estado_tutoria=et.id_estado_tutoria inner join facultades f on f.id_facultad=h.id_facultad inner join programas p on p.id_programa=h.id_programa inner join materias m on m.id_materia=h.id_materia inner join salones s on s.id_salon=h.id_salon inner join capacidades c on c.id_capacidad=s.id_capacidad inner join docentes d on d.id_usuario=h.id_usuario inner join sedes se on se.id_sede=h.id_sede where le.id_usuario={id_usuario} and et.estado_tutoria='pendiente'

            """
            cursor.execute(sql)
            return cursor.fetchall()
    
    except Exception as Error:
        print(Error)


def obtenerCupos(id_tutoria):
      bd=getConecction()
      cursor=bd.cursor()
      sql=f"SELECT h.cupos  from horario_tutorias h where id_tutoria={id_tutoria}"
      cursor.execute(sql)
      return cursor.fetchone()[0]

def cancelarTutorias(id_tutoria,id_usuario):
     bd=getConecction()
     cursor=bd.cursor()
     sql=f"DELETE FROM lista_estudiantes WHERE id_usuario={id_usuario} and id_tutoria={id_tutoria}"
     cursor.execute(sql)
     bd.commit()

def getTutoriaForId(id_tutoria:str):
    bd=getConecction()
    cursor=bd.cursor()
    sql=f"""select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,h.fecha_generacion_tutoria,f.facultad,p.programa,m.materia,s.sede,et.estado_tutoria,sa.salon,h.id_tutoria,c.capacidad from horario_tutorias h join facultades f on h.id_facultad=f.id_facultad join programas p on h.id_programa=p.id_programa join materias m on h.id_materia=m.id_materia join sedes s on h.id_sede=s.id_sede join salones sa on h.id_salon=sa.id_salon  join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria 
join capacidades c on c.id_capacidad=sa.id_capacidad
WHERE h.id_tutoria={id_tutoria}"""
    cursor.execute(sql)
    return cursor.fetchall()
 

