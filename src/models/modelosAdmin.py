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


