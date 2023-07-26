import mysql.connector
from werkzeug.security import generate_password_hash
import random
class Forgot():

    def __init__(self,bd:mysql.connector.connection.MySQLConnection):
        self.bd=bd
        self.cursor=bd.cursor()

    def generatePasswordHash(self,password):
       return generate_password_hash(password)


    def findRole(self,correo):
        sql=f"select id_rol from usuarios where correo='{correo}'"
        self.cursor.execute(sql)
        id_rol=self.cursor.fetchone()[0]
        return id_rol
    
    def updatePassword(self,correo,password):
        sql=f"update usuarios set contraseña='{password}' where correo='{correo}'"
        self.cursor.execute(sql)
        self.bd.commit()


    def getPassword(self):
        minusculas="abcdefghijklmnopqrstuvwxyz"
        mayusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        simbolos="@()[]{}*;/-_¿?!¡$"
        base=minusculas+mayusculas+simbolos
        longitud_contraseña=10
        password=random.sample(base,longitud_contraseña)
        passwordComplete="".join(password)
        return passwordComplete
