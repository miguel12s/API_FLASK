from databases.conexion import getConecction
from models.user import User
mybd=getConecction()
cursor=mybd.cursor()
def insertarEstudiante(estudiante):
       cursor.execute(f"INSERT INTO estudiantes( id_usuario ,nombres, apellidos, tipo_documento, numero_documento, celular, facultad, programa, correo) VALUES ( '{estudiante.id}','{estudiante.nombre}','{estudiante.apellido}','{estudiante.tipoDocumento}','{estudiante.numeroDocumento}','{estudiante.celular}','{estudiante.facultad}','{estudiante.programa}','{estudiante.correo[0]}')")
       mybd.commit()
       


def searchUserForRol(passwordHashed,data):
       password=User.checkPassword(passwordHashed[0],data['contraseña'])
       
       if(password):
              cursor.execute(f"select id_rol,id_usuario from usuarios where correo='{data['correo']}'and contraseña='{passwordHashed[0]}'")
              datos=cursor.fetchall()

              primer_fila = datos[0]
              id_rol = primer_fila[0]
              id_usuario = primer_fila[1]
              return id_usuario,id_rol
       else:
              print('el usuario no ha sido encontrado')
       return False,False

# def selectDataForIdUser(id_user):
#        cursor.execute(f"select * from estudiantes where id_usuario={id_user}")
#        data=cursor.fetchall()
#        return data

def getPasswordHash(correo):
       print(correo)
       sql=f"select contraseña from usuarios where correo='{correo}'"
       cursor.execute(sql)
       password= cursor.fetchone()
       print('la contraseña es',password)
       return password

def getPasswordForId(id_usuario):
       sql=f"select contraseña from usuarios where id_usuario='{id_usuario}'"
       cursor.execute(sql)
       password=cursor.fetchone()[0]
       print(password)
       return password    

def updatePassword(id,password):
       print('hash',password)
       sql=f"update usuarios set contraseña='{password}' where id_usuario='{id}'"
       cursor.execute(sql)
       mybd.commit()




        
    