
from databases.conexion import getConecction
from werkzeug.security import generate_password_hash

bd=getConecction()
cursor=bd.cursor()

class Docente:
    id:str
    nombre:str
    apellido:str
    tipoDocumento:str
    numeroDocumento=str
    celular:str
    facultad:str
    correo:str
    
    
    def __init__(self,id,nombre,apellido,tipoDocumento, numeroDocumento ,celular,facultad,correo) :
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.tipoDocumento=tipoDocumento
        self.numeroDocumento=numeroDocumento
        self.celular=celular
        self.facultad=facultad
        self.correo=correo
    @classmethod
    def save(self,docente):
        sql=f" INSERT INTO docentes (id_usuario, nombres, apellidos, tipo_documento, numero_documento, celular, facultad, correo) VALUES ('{docente.id}','{docente.nombre}','{docente.apellido}','{docente.tipoDocumento}','{docente.numeroDocumento}','{docente.celular}','{docente.facultad}','{docente.correo}')"
        cursor.execute(sql)
        bd.commit()
    def get(id_docente):
        sql=f"select * from docentes where id_usuario='{id_docente}'"
        cursor.execute(sql)
        docente=cursor.fetchone()
        print(docente)
        return Docente(docente[0],docente[1],docente[2],docente[3],docente[4],docente[5],docente[6],docente[7])

    def serialize(self):
        return {
                'id': self.id,
                'nombre': self.nombre,
                'apellido': self.apellido,
                'tipoDocumento': self.tipoDocumento,
                'numeroDocumento': self.numeroDocumento,
                'numeroTelefono': self.celular,
                'facultad':self.facultad,
                'correo':self.correo,
            }
 