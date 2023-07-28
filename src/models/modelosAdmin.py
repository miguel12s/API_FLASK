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
           
