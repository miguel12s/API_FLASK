from databases.conexion import getConecction



class consultasHorario():
    @classmethod
    def mostrarHorario(self, ids):
        mybd = getConecction()
        cursor = mybd.cursor()


        tutorias=[]
        for i in ids:
                
                id_facultad, id_programa, id_materia, id_sede, id_salon, id_estado_tutoria,id_tutoria = i
                
                sql = f"select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,h.fecha_generacion_tutoria,f.facultad,p.programa,m.materia,s.sede,et.estado_tutoria,sa.salon,h.id_tutoria from horario_tutorias h join facultades f on h.id_facultad=f.id_facultad join programas p on h.id_programa=p.id_programa join materias m on h.id_materia=m.id_materia join sedes s on h.id_sede=s.id_sede join salones sa on h.id_salon=sa.id_salon  join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria WHERE h.id_facultad = {id_facultad} AND h.id_programa = {id_programa} AND h.id_materia = {id_materia} AND h.id_sede = {id_sede} AND h.id_salon = {id_salon} AND h.id_estado_tutoria = {id_estado_tutoria} and h.id_tutoria={id_tutoria} and et.estado_tutoria='pendiente'"
                cursor.execute(sql)
                data = cursor.fetchall()
                tutorias.extend(data)
     
        return tutorias
    @classmethod
    def mostrarHorarioEstado(self, ids):
        mybd = getConecction()
        cursor = mybd.cursor()


        tutorias=[]
        for i in ids:
                
                id_facultad, id_programa, id_materia, id_sede, id_salon, id_estado_tutoria,id_tutoria = i
                
                sql = f"select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,h.fecha_generacion_tutoria,f.facultad,p.programa,m.materia,s.sede,et.estado_tutoria,sa.salon,h.id_tutoria from horario_tutorias h join facultades f on h.id_facultad=f.id_facultad join programas p on h.id_programa=p.id_programa join materias m on h.id_materia=m.id_materia join sedes s on h.id_sede=s.id_sede join salones sa on h.id_salon=sa.id_salon  join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria WHERE h.id_facultad = {id_facultad} AND h.id_programa = {id_programa} AND h.id_materia = {id_materia} AND h.id_sede = {id_sede} AND h.id_salon = {id_salon} AND h.id_estado_tutoria = {id_estado_tutoria} and h.id_tutoria={id_tutoria} and et.estado_tutoria='terminado'"
                cursor.execute(sql)
                data = cursor.fetchall()
                tutorias.extend(data)
     
        return tutorias

    @classmethod
    def obtenerIds(self, id_usuario):
        mybd = getConecction()
        cursor = mybd.cursor()


        sql = f"select id_facultad,id_programa,id_materia,id_sede,id_salon,id_estado_tutoria,id_tutoria from horario_tutorias where id_usuario='{id_usuario}' "
        cursor.execute(sql)
        ids = cursor.fetchall()
        print(ids)
        return ids
    @classmethod
    def serialize(self,data):
        tutorias=[]
        for i in data:
              tutoria={"cupos":i[0],"tema":i[1],"fecha":i[2],"horaInicio":i[3],"horaFin":i[4],"fecha_generacion_tutoria":i[5],"facultad":i[6],"programa":i[7],"materia":i[8],"sede":i[9],"id_estado_tutoria":i[10],"salon":i[11],"id_tutoria":i[12]}
              tutorias.append(tutoria)
              print(tutorias)
        return tutorias
    @classmethod
    def serializeId(self,i):
        print(i)
        return {
            "cupos":i[0][0],"tema":i[0][1],"fecha":i[0][2],"horaInicio":i[0][3],"horaFin":i[0][4],"id_tutoria":i[0][5],"facultad":i[0][6],"programa":i[0][7],"materia":i[0][8],"sede":i[0][9],
                       
              "estado_tutoria":i[0][10],
              "nombres":i[0][11],
                       "apellidos":i[0][12],
                       "salon":i[0][13],
                       "capacidad":i[0][14],
                       "id_tutoria":i[0][15],
        }
    
    @classmethod
    def serializeTutoria(self,i):
         return {
              "cupos":i[0][0],"tema":i[0][1],"fecha":i[0][2],"horaInicio":i[0][3],"horaFin":i[0][4],"fecha_generacion_tutoria":i[0][5],"facultad":i[0][6],"programa":i[0][7],"materia":i[0][8],"sede":i[0][9],
                       
              "estado_tutoria":i[0][10],
                       "salon":i[0][11],
                       "id_tutoria":i[0][12],
                       "capacidad":i[0][13]
                       
         }