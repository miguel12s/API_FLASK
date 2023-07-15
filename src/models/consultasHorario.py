from databases.conexion import getConecction


mybd = getConecction()
cursor = mybd.cursor()


class consultasHorario():
    @classmethod
    def mostrarHorario(self, ids):

        sql = f"select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,h.fecha_generacion_tutoria,f.facultad,p.programa,m.materia,s.sede,et.estado_tutoria,sa.salon from horario_tutorias h join facultades f on h.id_facultad=f.id_facultad join programas p on h.id_programa=p.id_programa join materias m on h.id_materia=m.id_materia join sedes s on h.id_sede=s.id_sede join salones sa on h.id_salon=sa.id_salon  join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria WHERE h.id_facultad = {ids[0][0]} AND h.id_programa = {ids[0][1]} AND h.id_materia = {ids[0][2]} AND h.id_sede = {ids[0][3]} AND h.id_salon = {ids[0][4]} AND h.id_estado_tutoria = {ids[0][5]};"
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    @classmethod
    def obtenerIds(self, id_usuario):
        sql = f"select id_facultad,id_programa,id_materia,id_sede,id_salon,id_estado_tutoria from horario_tutorias where id_usuario='{id_usuario}' "
        cursor.execute(sql)
        ids = cursor.fetchall()
        print(ids)
        return ids
