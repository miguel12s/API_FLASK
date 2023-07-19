from databases.conexion import getConecction



def mostrarHorarioss():
    bd=getConecction()
    cursor=bd.cursor()
    sql="select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,h.id_tutoria,f.facultad,p.programa,m.materia,s.sede,et.estado_tutoria,doc.nombres,doc.apellidos,sal.salon,capa.capacidad,et.id_estado_tutoria from horario_tutorias h join facultades f on h.id_facultad=f.id_facultad join programas p on h.id_programa=p.id_programa join materias m on h.id_materia=m.id_materia join sedes s on h.id_sede=s.id_sede join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria join docentes doc on h.id_usuario=doc.id_usuario join salones sal on h.id_salon=sal.id_salon join capacidades capa on h.id_salon=capa.id_capacidad "
    cursor.execute(sql)
    horarios=cursor.fetchall()
    return horarios

def agendarTutoria(id_usuario,id_tutoria,id_estado_tutoria):
    bd=getConecction()
    cursor=bd.cursor()
    sql=f"INSERT INTO lista_estudiantes(id_tutoria, id_usuario, id_estado_tutoria) VALUES ('{id_tutoria}','{id_usuario}','{id_estado_tutoria}')"
    cursor.execute(sql)
    bd.commit()

def actualizarCupos(id_tutoria):
    bd=getConecction()
    cursor=bd.cursor()
    sql=f"UPDATE horario_tutorias SET cupos=cupos-1 WHERE id_tutoria={id_tutoria} "
    cursor.execute(sql)
    bd.commit()

def verificarListaDeEstudiantes(id_usuario):
    
    bd=getConecction()
    cursor=bd.cursor()
    try:
        sql=f"select id_tutoria from lista_estudiantes where id_usuario={id_usuario}"
        cursor.execute(sql)
        id_tutoria=cursor.fetchone()[0]
        if(id_tutoria)==None:
            return None
        else:
            return id_tutoria
    except :
        print("error")
    
