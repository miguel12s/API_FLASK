import mysql.connector
from datetime import datetime
from databases.conexion import getConecction



class ModelosAdmin():
    def __init__(self,bd:mysql.connector.connection.MySQLConnection):
        self.bd=bd
        self.cursor=bd.cursor()

    def agregarFacultad(self,facultad):
        sql=f"INSERT INTO facultades (facultad) VALUES ('{facultad}')"
        self.cursor.execute(sql)
        self.bd.commit()
    def obtenerFacultades(self):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f" SELECT `id_facultad`, `facultad` FROM `facultades` WHERE 1"
        cursor.execute(sql)
        data=cursor.fetchall()
        lista=[]
        for i in data:
            objeto={
                "id_facultad":i[0],
                "facultad":i[1]
            }
            lista.append(objeto)
            print(lista)
        return lista
    
    def actualizarFacultad(self,facultad):
        sql=f"update facultades set facultad='{facultad['facultad']}' where id_facultad={facultad['id_facultad']}"
        self.cursor.execute(sql)
        self.bd.commit()

    def obtenerFacultadPorId(self,id_facultad):
        sql=f"select * from facultades where id_facultad={id_facultad}"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        print(data)
        return {
            "id_facultad":data[0][0],
            "facultad":data[0][1]
        }
    






    def agregarPrograma(self,programa):
        sql=f"INSERT INTO programas (programa) VALUES ('{programa}')"
        self.cursor.execute(sql)
        self.bd.commit()
    def obtenerProgramas(self):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"select * from programas"
        cursor.execute(sql)
        data=cursor.fetchall()
        lista=[]
        for i in data:
            objeto={
                "id_programa":i[0],
                "programa":i[1]
            }
            lista.append(objeto)
        return lista
    
    def actualizarPrograma(self,programa):
        sql=f"update programas set programa='{programa['programa']}' where id_programa={programa['id_programa']}"
        self.cursor.execute(sql)
        self.bd.commit()

    def obtenerProgramaPorId(self,id_programa):
        sql=f"select * from programas where id_programa={id_programa}"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        print(data)
        return {
            "id_programa":data[0][0],
            "programa":data[0][1]
        }
    








    def agregarMateria(self,materia):
        sql=f"INSERT INTO materias (materia) VALUES ('{materia}')"
        self.cursor.execute(sql)
        self.bd.commit()
    def obtenerMaterias(self):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"SELECT `id_materia`, `materia` FROM `materias` WHERE 1"
        cursor.execute(sql)
        data=cursor.fetchall()
        lista=[]
        for i in data:
            objeto={
                "id_materia":i[0],
                "materia":i[1]
            }
            lista.append(objeto)
        return lista
    
    def actualizarMateria(self,materia):
        sql=f"update materias set materia='{materia['materia']}' where id_materia={materia['id_materia']}"
        self.cursor.execute(sql)
        self.bd.commit()

    def obtenerMateriaPorId(self,id_materia):
        sql=f"select * from materias where id_materia={id_materia}"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        print(data)
        return {
            "id_materia":data[0][0],
            "materia":data[0][1]
        }
    def getSedes(self):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"SELECT `id_sede`, `sede` FROM `sedes` WHERE 1"
        cursor.execute(sql)
        sedes=cursor.fetchall()
        listaSedes=[]
        for i in sedes:
            sede={
                "id_sede":i[0],
                "sede":i[1]

            }
            listaSedes.append(sede)
        return listaSedes    
    def obtenerSedePorId(self,id_sede:str):
        sql=f"select * from sedes where id_sede={id_sede} "
        self.cursor.execute(sql)
        sede=self.cursor.fetchall()
        return {
            "id_sede":sede[0][0],
            "sede":sede[0][1]
        }
    def agregarSede(self,sede):
        sql=f"INSERT INTO sedes (sede) VALUES ('{sede}')"
        self.cursor.execute(sql)
        self.bd.commit()
    
    def actualizarSede(self,data):
         sql=f"update sedes set sede='{data['sede']}' where id_sede={data['id_sede']}"
         self.cursor.execute(sql)
         self.bd.commit()

    def getSalones(self):
        sql="SELECT c.capacidad,s.salon,se.sede,s.id_salon FROM salones s join capacidades c on s.id_capacidad=c.id_capacidad join sedes se on s.id_sede=se.id_sede"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        print(data)
        salones=[]
        for i in data:
            salon={
                "capacidad":i[0],
                "salon":i[1],
                "sede":i[2],
                "id_salon":i[3]
            }
            salones.append(salon)
        return salones
    
    def getRoles(self):
        sql="select * from roles"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        roles=[]
        for i in data:
            rol={
                "id_rol":i[0],
                "rol":i[1],
                
            }
            roles.append(rol)
        return roles
    


    def obtenerSalonPorId(self,id_salon:str):
        sql=f"""select c.capacidad,s.salon,se.sede,s.id_salon from salones s
join capacidades c on s.id_capacidad=c.id_capacidad
join sedes se on s.id_sede=se.id_sede where s.id_salon={id_salon} """
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        return {
                "capacidad":data[0][0],
                "salon":data[0][1],
                "sede":data[0][2],
                "id_salon":data[0][3]
            }
    
    # def agregarSalon(self,body):
    #     sql="insert into sal"
           
    def obtenerRolPorId(self,id_rol):
        sql=f"""select * from roles where id_rol={id_rol} """
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        return {
                "rol":data[0][1],
                "id_rol":data[0][0]
            }
    def setRol(self,rol):
        print(rol)
        sql=f"insert into roles (rol) values ('{rol['rol']}')"
        print(sql)
        self.cursor.execute(sql)
        self.bd.commit()

    def actualizarRol(self,roles):
        sql=f"update roles set rol='{roles['rol']}' where id_rol={roles['id_rol']}"
        self.cursor.execute(sql)
        self.bd.commit()






    def obtenerTipoPorId(self,id_tipo:str):
        sql=f"""select * from tipos_documento where id_tipo_documento={id_tipo} """
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        return {
               "id_tipo_documento":data[0][0],
               "tipo_documento":data[0][1]
            }
    
    
    def getTipo(self):
        bd=getConecction()
        cursor=bd.cursor()
        sql="select * from tipos_documento"
        cursor.execute(sql)
        data=cursor.fetchall()
        tipo_documento=[]
        for i in data:
            tipo={
                "id_tipo_documento":i[0],
                "tipo_documento":i[1],
                
            }
            tipo_documento.append(tipo)
        return tipo_documento
    
    def setTipo(self,tipo):
        
        sql=f"insert into tipos_documento (tipo_documento) values ('{tipo['tipo_documento']}')"
        print(sql)
        self.cursor.execute(sql)
        self.bd.commit()

    def actualizarTipo(self,data):
        sql=f"update tipos_documento set tipo_documento='{data['tipo_documento']}' where id_tipo_documento={data['id_tipo_documento']}"
        self.cursor.execute(sql)
        self.bd.commit()   
    
    def getEstado(self):
          
        bd=getConecction()
        cursor=bd.cursor()
        sql="select * from estados"
        cursor.execute(sql)
        data=cursor.fetchall()
        estados=[]
        for i in data:
            estado={
                "id_estado":i[0],
                "estado":i[1]
            }
            estados.append(estado)
        return estados


        
    def obtenerEstadoPorId(self,id_estado:str):
        sql=f"""select * from estados where id_estado={id_estado} """
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        return {
               "id_estado":data[0][0],
               "estado":data[0][1]
            }
    def setEstado(self,estados):
        
        sql=f"insert into estados (estado) values ('{estados['estado']}')"
        self.cursor.execute(sql)
        self.bd.commit()

    def actualizarEstado(self,estado):
        print(estado)
        sql=f"update estados set estado='{estado['estado']}' where id_estado={estado['id_estado']}"
        self.cursor.execute(sql)
        self.bd.commit()




    def getEstadoTutoria(self):
        sql="select * from estados_tutorias"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        estados=[]
        for i in data:
            estado={
                "id_estado_tutoria":i[0],
                "estado_tutoria":i[1]
            }
            estados.append(estado)
        return estados


        
    def obtenerEstadoTutoriaPorId(self,id_estado_tutoria:str):
        sql=f"""select * from estados_tutorias where id_estado_tutoria={id_estado_tutoria} """
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        return {
               "id_estado_tutoria":data[0][0],
               "estado_tutoria":data[0][1]
            }
    def setEstadoTutoria(self,estados):
        
        sql=f"insert into estados_tutorias (estado_tutoria) values ('{estados['estado_tutoria']}')"
        self.cursor.execute(sql)
        self.bd.commit()

    def actualizarEstadoTutoria(self,estado):
        print(estado)
        sql=f"update estados_tutorias set estado_tutoria='{estado['estado_tutoria']}' where id_estado_tutoria={estado['id_estado_tutoria']}"
        self.cursor.execute(sql)
        self.bd.commit()


    def getCapacidad(self):
        sql="select * from capacidades"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        capacidades=[]
        for i in data:
            capacidad={
                "id_capacidad":i[0],
                "capacidad":i[1]
            }
            capacidades.append(capacidad)
        return capacidades


        
    def obtenerCapacidadPorId(self,id_capacidad:str):
        sql=f"""select * from capacidades where id_capacidad={id_capacidad} """
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        return {
               "id_capacidad":data[0][0],
               "capacidad":data[0][1]
            }
    def setCapacidad(self,capacidad):
        
        sql=f"insert into capacidades (capacidad) values ('{capacidad['capacidad']}')"
        self.cursor.execute(sql)
        self.bd.commit()

    def actualizarCapacidad(self,capacidad):
        print(capacidad)
        sql=f"update capacidades set capacidad='{capacidad['capacidad']}' where id_capacidad={capacidad['id_capacidad']}"
        self.cursor.execute(sql)
        self.bd.commit()   



    def obtenerIds(self,salon):
        print(salon)
        sql=f"""
SELECT c.id_capacidad,se.id_sede from capacidades c
join sedes se on se.id_sede=se.id_sede
where c.capacidad='{salon['capacidad']}' and se.sede='{salon['sede']}'"""
        print(sql)
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        print(data)
        return {
            "id_capacidad":data[0][0],
            "id_sede":data[0][1],
        }
    def agregarSalon(self,ids,salon):
        
        sql=f"INSERT INTO salones( id_capacidad, salon, id_sede) VALUES ({ids['id_capacidad']},'{salon}',{ids['id_sede']})"
        self.cursor.execute(sql)
        self.bd.commit() 


    def actualizarSalon(self,ids,salon):
        
        sql=f"""update salones set id_capacidad={ids['id_capacidad']}, salon='{salon['salon']}',id_sede={ids['id_sede']} where id_salon={salon['id_salon']}"""
        print(sql)
        self.cursor.execute(sql)
        self.bd.commit()
    
    def getHorario(self):
        bd=getConecction()
        cursor=bd.cursor()
        sql="""
        select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,h.id_tutoria,f.facultad,p.programa,m.materia,s.sede,et.id_estado_tutoria,doc.nombres,doc.apellidos,sal.salon,capa.capacidad,h.id_tutoria,doc.id_usuario from horario_tutorias h join facultades f on h.id_facultad=f.id_facultad join programas p on h.id_programa=p.id_programa join materias m on h.id_materia=m.id_materia join sedes s on h.id_sede=s.id_sede join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria join docentes doc on h.id_usuario=doc.id_usuario join salones sal on h.id_salon=sal.id_salon join capacidades capa on sal.id_capacidad=capa.id_capacidad where et.id_estado_tutoria=1"""
        cursor.execute(sql)
        data=cursor.fetchall()
        print('horario',data)
        horarios=[]
      
        for i in data:
          horario={
              
"cupos":i[0],	
"tema":i[1],	
"fecha":i[2],	
"hora_inicial":i[3],	
"hora_final":i[4],	
"id_tutoria":i[5],	
"facultad":i[6],	
"programa":i[7],	
"materia":i[8],	
"sede":i[9],	
"id_estado_tutoria":i[10],	
"nombres":i[11],	
"apellidos":i[12],	
"salon":i[13],	
"capacidad":i[14],	
"id_tutoria":i[15],
"id_docente":i[16]
          }
          horarios.append(horario)
        print(horarios)
        return horarios
    

    def obtenerIdsTabla(self,data):
       
        sql=f"""SELECT
  (SELECT id_programa FROM programas WHERE programa = "{data['programa']}") AS id_programa,
  (SELECT id_sede FROM sedes WHERE sede = "{data['sede']}") AS id_sede,
  (SELECT id_salon FROM salones WHERE salon = "{data['salon']}") AS id_salon,
   (SELECT id_usuario FROM docentes WHERE nombres = "{data['docente']}") AS id_salon,
  (SELECT id_capacidad FROM capacidades WHERE capacidad = {data['capacidad']}) AS id_capacidad,
  (SELECT id_materia FROM materias WHERE materia = "{data['materia']}") AS id_materia,
  (SELECT id_facultad FROM facultades WHERE facultad = "{data['facultad']}") AS id_facultad;


 """
        
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        print(data)
        return {
            "id_programa":data[0][0],
            "id_sede":data[0][1],
            "id_salon":data[0][2],
            "id_capacidad":data[0][3],
            "id_usuario":data[0][4],
            "id_materia":data[0][5],
            "id_facultad":data[0][6]
        }
    def actualizarTutoria(self,horario,ids):
        id_docente=horario['docente'].split('-')[1]
        print(horario['id_tutoria'])
        sql=f"UPDATE horario_tutorias set id_programa='{ids['id_programa']}',id_materia='{ids['id_materia']}',id_sede='{ids['id_sede']}',id_salon='{ids['id_salon']}',tema='{horario['tema']}',fecha='{horario['fecha']}',hora_inicial='{horario['horaInicio']}',hora_final='{horario['horaFin']}',id_facultad='{ids['id_facultad']}',id_usuario='{id_docente}' WHERE id_tutoria={horario['id_tutoria']}"
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
    def getDocente(self):
        bd=getConecction()
        cursor=bd.cursor()
        sql="SELECT nombres,apellidos,id_usuario FROM `docentes` WHERE 1"
        cursor.execute(sql)
        data=cursor.fetchall()
        docentes=[]
        for i in data:
            docente={
                "nombres":f"{i[0]} {i[1]}",
                "id_docente":i[2]
            }
            docentes.append(docente)
        print(docentes)
        return docentes
    def crearHorario(self,horario,ids):
        id_usuario=horario['docente'].split('-')[1]
        fecha=datetime.now()
        print(fecha)
        sql=f"insert into horario_tutorias (id_tutoria, id_facultad, id_programa, id_materia, id_sede, id_salon, id_usuario, id_estado_tutoria, cupos, tema, fecha, hora_inicial, hora_final) VALUES ('{0}','{ids['id_facultad']}','{ids['id_programa']}','{ids['id_materia']}','{ids['id_sede']}','{ids['id_salon']}','{id_usuario}','{1}','{horario['capacidad']}','{horario['tema']}','{horario['fecha']}','{horario['horaInicio']}','{horario['horaFin']}')"
        self.cursor.execute(sql)
        self.bd.commit()
    


    def getHorarioFinished(self):
            bd=getConecction()
            cursor=bd.cursor()
            sql="""
            select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,h.id_tutoria,f.facultad,p.programa,m.materia,s.sede,et.id_estado_tutoria,doc.nombres,doc.apellidos,sal.salon,capa.capacidad,h.id_tutoria,doc.id_usuario,h.fecha_generacion_tutoria from horario_tutorias h join facultades f on h.id_facultad=f.id_facultad join programas p on h.id_programa=p.id_programa join materias m on h.id_materia=m.id_materia join sedes s on h.id_sede=s.id_sede join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria join docentes doc on h.id_usuario=doc.id_usuario join salones sal on h.id_salon=sal.id_salon join capacidades capa on sal.id_capacidad=capa.id_capacidad where et.id_estado_tutoria=2"""
            cursor.execute(sql)
            data=cursor.fetchall()
            horarios=[]
        
            for i in data:
                horario={
                    
        "cupos":i[0],	
        "tema":i[1],	
        "fecha":i[2],	
        "hora_inicial":i[3],	
        "hora_final":i[4],	
        "id_tutoria":i[5],	
        "facultad":i[6],	
        "programa":i[7],	
        "materia":i[8],	
        "sede":i[9],	
        "id_estado_tutoria":i[10],	
        "nombres":i[11],	
        "apellidos":i[12],	
        "salon":i[13],	
        "capacidad":i[14],	
        "id_tutoria":i[15],
        "id_docente":i[16],
        "fecha_generacion_tutoria":i[17]
                }
                
                horarios.append(horario)
            return horarios
    
    def getEstudiantes(self):
        bd=getConecction()
        cursor=bd.cursor()
        sql="""SELECT es.nombres,es.celular,es.correo,es.facultad,u.id_estado,u.id_usuario FROM estudiantes es 
join usuarios u  on es.id_usuario=u.id_usuario  ORDER BY (es.nombres)
 """
        cursor.execute(sql)
        data=cursor.fetchall()
        estudiantes=[]
        for i in data:
            estudiante={
                "nombres":i[0],
                "celular":i[1],
                "correo":i[2],
                "facultad":i[3],
                "id_estado":i[4],
                "id_usuario":i[5],
            }
            estudiantes.append(estudiante) 
        return estudiantes
    def getEstudiante(self,id_usuario):
        sql=f"""SELECT es.nombres, 
        es.apellidos,es.tipo_documento,es.numero_documento,es.programa,es.facultad,
        es.celular,es.correo,es.facultad,u.id_estado,u.id_usuario,e.estado FROM estudiantes es 
join usuarios u  on es.id_usuario=u.id_usuario
join estados e on e.id_estado=u.id_estado
where es.id_usuario={id_usuario}

  ORDER BY (es.nombres)
 """
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        
        
        estudiante={
                "nombres":data[0][0],
                "apellidos":data[0][1],
                "tipo_documento":data[0][2],
                "numero_documento":data[0][3],
                "programa":data[0][4],
                "facultad":data[0][5],
                "celular":data[0][6],
                "correo":data[0][7],
                "facultad":data[0][8],
                "id_estado":data[0][9],
                "id_usuario":data[0][10],
                "estado":data[0][11]
            }
        return estudiante
    def getEstadoForEstado(self,estado):
        sql=f"select id_estado from estados where estado='{estado}'"
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def actualizarUsuario(self,id_estudiante,id_estado,correo):
        sql=f" update usuarios set id_estado={id_estado} , correo='{correo}' where id_usuario={id_estudiante}"
        self.cursor.execute(sql)
        self.bd.commit()
    def actualizarEstudiante(self,id_estudiante,data):
        sql=f"UPDATE `estudiantes` SET `nombres`='{data['nombres']}',`apellidos`='{data['apellidos']}',`tipo_documento`='{data['tipo_documento']}',`numero_documento`='{data['numero_documento']}',`celular`='{data['celular']}',`facultad`='{data['facultad']}',`programa`='{data['programa']}',`correo`='{data['correo']}' WHERE id_usuario={id_estudiante}"
        self.cursor.execute(sql)
        self.bd.commit()
    def getDocentess(self):
        bd=getConecction()
        cursor=bd.cursor()
        sql="""SELECT es.nombres,es.celular,es.correo,es.facultad,u.id_estado,u.id_usuario,es.apellidos FROM docentes es 
join usuarios u  on es.id_usuario=u.id_usuario  ORDER BY (es.nombres)"""
        cursor.execute(sql)
        data=cursor.fetchall()
        print(data)
        docentes=[]
        for i in data:
            docente={
                "nombres":i[0],
                "facultad":i[3],
                "celular":i[1],
                "correo":i[2],
                "facultad":i[3],
                "id_estado":i[4],
                "id_usuario":i[5],
                "apellidos":i[6]
                
            }
            docentes.append(docente)
        return docentes
    def getDocenteFull(self,id_usuario):
        bd=getConecction()
        cursor=bd.cursor()
        sql=f"""
SELECT es.nombres, 
        es.apellidos,es.tipo_documento,es.numero_documento,es.facultad,
        es.celular,es.correo,u.id_estado,u.id_usuario,e.estado FROM docentes es 
join usuarios u  on es.id_usuario=u.id_usuario
join estados e on e.id_estado=u.id_estado
where es.id_usuario={id_usuario}

  ORDER BY (es.nombres)
"""
        cursor.execute(sql)
        data=cursor.fetchall()
        print(data)
        return {
            "nombres":data[0][0],
            "apellidos":data[0][1],
            "tipo_documento":data[0][2],
            "numero_documento":data[0][3],
            "facultad":data[0][4],
            "celular":data[0][5],
            "correo":data[0][6],
            "id_estado":data[0][7],
            "id_usuario":data[0][8],
            "estado":data[0][9]
        }
    def actualizarDocente(self,id_estudiante,data):
        sql=f"""
UPDATE `docentes` SET `nombres`='{data['nombres']}',`apellidos`='{data['apellidos']}',`tipo_documento`='{data['tipo_documento']}',`numero_documento`='{data['numero_documento']}',`celular`='{data['celular']}',`facultad`='{data['facultad']}',`correo`='{data['correo']}' WHERE id_usuario={id_estudiante}
"""
        self.cursor.execute(sql)
        self.bd.commit()
