from databases.conexion import getConecction

bd=getConecction()
cursor=bd.cursor()

def mostrarHorarioss():
    sql="select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,h.id_tutoria,f.facultad,p.programa,m.materia,s.sede,et.estado_tutoria,doc.nombres,doc.apellidos,sal.salon,capa.capacidad from horario_tutorias h join facultades f on h.id_facultad=f.id_facultad join programas p on h.id_programa=p.id_programa join materias m on h.id_materia=m.id_materia join sedes s on h.id_sede=s.id_sede join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria join docentes doc on h.id_usuario=doc.id_usuario join salones sal on h.id_salon=sal.id_salon join capacidades capa on h.id_salon=capa.id_capacidad "
    cursor.execute(sql)
    horarios=cursor.fetchall()
    return horarios

