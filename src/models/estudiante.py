from databases.conexion import getConecction
from werkzeug.security import generate_password_hash
from models.modelos import saveFoto
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
    foto:str
    

    def __init__(self,id,nombre,apellido,tipoDocumento, numeroDocumento ,celular,facultad,programa,correo,foto) :
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.tipoDocumento=tipoDocumento
        self.numeroDocumento=numeroDocumento
        self.celular=celular
        self.facultad=facultad
        self.programa=programa
        self.correo=correo,
        self.foto=foto


    @classmethod
    def save(self,estudiante):
        print(estudiante.correo)
        sql=f"INSERT INTO estudiantes( id_usuario ,nombres, apellidos, tipo_documento, numero_documento, celular, facultad, programa, correo,foto) VALUES ( '{estudiante.id}','{estudiante.nombre}','{estudiante.apellido}','{estudiante.tipoDocumento}','{estudiante.numeroDocumento}','{estudiante.celular}','{estudiante.facultad}','{estudiante.programa}','{estudiante.correo[0]}','{'ubsolo.png'}')" 
        cursor.execute(sql)
        bd.commit()
    def get(id_estudiante):
        sql=f"select * from estudiantes where id_usuario='{id_estudiante}'"
        cursor.execute(sql)
        estudiante=cursor.fetchone()
        print('imagen estudiante',estudiante[9])
        return Estudiante(estudiante[0],estudiante[1],estudiante[2],estudiante[3],estudiante[4],estudiante[5],estudiante[6],estudiante[7],estudiante[8],estudiante[9])
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'tipoDocumento': self.tipoDocumento,
            'numeroDocumento': self.numeroDocumento,
            'numeroTelefono': self.celular,
            'facultad':self.facultad,
            'programa':self.programa,
            'correo':self.correo,
            'foto':self.foto
        }
    @classmethod
    def updateImage(self,image,id_user):
        saveFoto(image,id_user)
 

    