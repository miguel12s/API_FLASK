from databases.conexion import getConecction


bd=getConecction()
cursor=bd.cursor()
class Estudiante:
    id:str
    nombre:str
    apellido:str
    tipoDocumento:str
    numeroDocumento=str
    celular:str
    facultad:str
    programa:str
    correo:str
    

    def __init__(self,id,nombre,apellido,tipoDocumento, numeroDocumento ,celular,facultad,programa,correo) :
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.tipoDocumento=tipoDocumento
        self.numeroDocumento=numeroDocumento
        self.celular=celular
        self.facultad=facultad
        self.programa=programa
        self.correo=correo

    @classmethod
    def save(self,estudiante):
        sql=f"INSERT INTO estudiantes( id_usuario ,nombres, apellidos, tipo_documento, numero_documento, celular, facultad, programa, correo) VALUES ( '{estudiante.id}','{estudiante.nombre}','{estudiante.apellido}','{estudiante.tipoDocumento}','{estudiante.numeroDocumento}','{estudiante.celular}','{estudiante.facultad}','{estudiante.programa}','{estudiante.correo}')"   
        cursor.execute(sql)
        bd.commit()

    