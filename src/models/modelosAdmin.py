import mysql.connector



class ModelosAdmin():
    def __init__(self,bd:mysql.connector.connection.MySQLConnection):
        self.bd=bd
        self.cursor=bd.cursor()

    def agregarFacultad(self,facultad):
        sql=f"INSERT INTO facultades (facultad) VALUES ('{facultad}')"
        self.cursor.execute(sql)
        self.bd.commit()
    def obtenerFacultades(self):
        sql=f"select  * from facultades"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
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
        sql=f"select  * from programas"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
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
        sql=f"select  * from materias"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
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
        sql=f"select * from sedes "
        self.cursor.execute(sql)
        sedes=self.cursor.fetchall()
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
        sql="select c.capacidad,s.salon,se.sede,s.id_salon from salones s join capacidades c on s.id_capacidad=c.id_capacidad join sedes se on s.id_sede=se.id_sede"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
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
        sql="select * from tipos_documento"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
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
        sql="select * from estados"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
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