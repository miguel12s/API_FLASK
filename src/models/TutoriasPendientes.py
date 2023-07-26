import mysql.connector

class TutoriasPendientes():
    def __init__(self,bd:mysql.connector.connection.MySQLConnection):
        self.bd=bd
        self.cursor=bd.cursor()


    def TutoriasPendientes(self,id_usuario):
        sql=f"select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,le.id_tutoria,f.facultad ,p.programa,m.materia,se.sede,et.estado_tutoria,d.nombres,d.apellidos,s.salon,c.capacidad , s.salon,c.capacidad ,d.nombres,d.apellidos,et.id_estado_tutoria from lista_estudiantes le inner join horario_tutorias h on h.id_tutoria=le.id_tutoria inner join estados_tutorias et on le.id_estado_tutoria=et.id_estado_tutoria inner join facultades f on f.id_facultad=h.id_facultad inner join programas p on p.id_programa=h.id_programa inner join materias m on m.id_materia=h.id_materia inner join salones s on s.id_salon=h.id_salon inner join capacidades c on c.id_capacidad=s.id_capacidad inner join docentes d on d.id_usuario=h.id_usuario inner join sedes se on se.id_sede=h.id_sede where le.id_usuario={id_usuario} AND et.estado_tutoria='terminado' "
        self.cursor.execute(sql)
        tutoriasPendientes= self.cursor.fetchall()
        return tutoriasPendientes
    def listadoEstudiantes(self,id_tutoria):
        sql=f"""select e.nombres,e.apellidos,e.numero_documento,e.programa from horario_tutorias ht
join lista_estudiantes le on ht.id_tutoria=le.id_tutoria
join estudiantes e on le.id_usuario=e.id_usuario 
where le.id_tutoria={id_tutoria}"""
        self.cursor.execute(sql)
        data= self.cursor.fetchall()
        listados=[]
        for i in data:
            listado={
                "nombres":data[0][0],
                "apellidos":data[0][1],
                "identificacion":data[0][2],
                "programa":data[0][3]
            }
            listados.append(listado)
        return listados
