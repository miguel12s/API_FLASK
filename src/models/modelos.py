from databases.conexion import getConecction
from models.estudiante import Estudiante
mybd=getConecction()
cursor=mybd.cursor()
def insertarUsuario(estudiante:Estudiante):
       print(estudiante)
       cursor.execute(f"INSERT INTO estudiante(nombre,apellido) VALUES ('{estudiante['nombre']}','{estudiante['apellido']}')")
       mybd.commit
        
        
       
        
    