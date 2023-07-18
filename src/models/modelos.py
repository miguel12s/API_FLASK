from databases.conexion import getConecction
from models.user import User
from models.horario import Horario

def insertarEstudiante(estudiante):
       mybd=getConecction()
       cursor=mybd.cursor() 
       cursor.execute(f"INSERT INTO estudiantes( id_usuario ,nombres, apellidos, tipo_documento, numero_documento, celular, facultad, programa, correo) VALUES ( '{estudiante.id}','{estudiante.nombre}','{estudiante.apellido}','{estudiante.tipoDocumento}','{estudiante.numeroDocumento}','{estudiante.celular}','{estudiante.facultad}','{estudiante.programa}','{estudiante.correo[0]}')")
       mybd.commit()
       


def searchUserForRol(passwordHashed,data):
       mybd=getConecction()
       cursor=mybd.cursor()
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
       mybd=getConecction()
       cursor=mybd.cursor()
       print(correo)
       sql=f"select contraseña from usuarios where correo='{correo}'"
       cursor.execute(sql)
       password= cursor.fetchone()
       print('la contraseña es',password)
       return password

def getPasswordForId(id_usuario):
       mybd=getConecction()
       cursor=mybd.cursor()
       sql=f"select contraseña from usuarios where id_usuario='{id_usuario}'"
       cursor.execute(sql)
       password=cursor.fetchone()[0]
       print(password)
       return password    

def updatePassword(id,password):
       print('hash',password)
       mybd=getConecction()
       cursor=mybd.cursor()
       sql=f"update usuarios set contraseña='{password}' where id_usuario='{id}'"
       cursor.execute(sql)
       mybd.commit()

def saveFoto(img,id_user):
       mybd=getConecction()
       cursor=mybd.cursor()
       sql=f"update estudiantes set foto='{img}' where id_usuario='{id_user}'"
       cursor.execute(sql)
       mybd.commit()

def saveFotoDocente(img,id_user):
       mybd=getConecction()
       cursor=mybd.cursor()
       sql=f"update docentes set foto='{img}' where id_usuario='{id_user}'"
       cursor.execute(sql)
       mybd.commit()

def getLittleDataForTeacher(id_teacher):
       mybd=getConecction()
       cursor=mybd.cursor()
       sql=f"select nombres,apellidos,facultad from docentes where id_usuario='{id_teacher}'"
       cursor.execute(sql)
       data=cursor.fetchone()[0]
       dataJson=Horario.serialize(data)
       print(dataJson)
       return dataJson
       
def getIdRol(id_usuario):
       mybd=getConecction()
       cursor=mybd.cursor()
       sql=f"select id_rol from usuarios where id_usuario='{id_usuario}'"
       cursor.execute(sql)
       data=cursor.fetchone()[0]
       
       return data


def getHorarioForId(id_usuario):
       mybd=getConecction()
       cursor=mybd.cursor()
       sql=f"select h.cupos,h.tema,h.fecha,h.hora_inicial,h.hora_final,h.id_tutoria,f.facultad,p.programa,m.materia,s.sede,et.estado_tutoria,doc.nombres,doc.apellidos,sal.salon,capa.capacidad from horario_tutorias h join facultades f on h.id_facultad=f.id_facultad join programas p on h.id_programa=p.id_programa join materias m on h.id_materia=m.id_materia join sedes s on h.id_sede=s.id_sede join estados_tutorias et on h.id_estado_tutoria=et.id_estado_tutoria join docentes doc on h.id_usuario=doc.id_usuario join salones sal on h.id_salon=sal.id_salon join capacidades capa on h.id_salon=capa.id_capacidad where h.id_tutoria={id_usuario}"
       cursor.execute(sql)
       data=cursor.fetchall()
       
       return data


        
    