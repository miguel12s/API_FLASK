from werkzeug.security import check_password_hash, generate_password_hash
from databases.conexion import getConecction
from flask_login import UserMixin

bd = getConecction()
cursor = bd.cursor()


class User(UserMixin):
    id_rol: int
    id_estado: int
    id:int
    correo: str
    contraseña: str

    def __init__(self, id, id_rol, id_estado, correo, contraseña) -> None:
        self.id = id
        self.id_rol = id_rol
        self.id_estado = id_estado
        self.correo = correo
        self.contraseña = generate_password_hash(contraseña)

    @classmethod
    def save(self, usuario):
        sql = f"INSERT INTO usuarios (id_usuario, id_rol, id_estado, correo, contraseña) VALUES ('{None}', '{usuario.id_rol}', '{1}', '{usuario.correo}', '{usuario.contraseña}')"
        cursor.execute(sql)
        bd.commit()
        id_usuario = cursor.lastrowid
        print(id_usuario)
        return id_usuario

    @classmethod
    def checkPassword(self, passwordHashed, password):
        return check_password_hash(passwordHashed, password)

    @classmethod

    def generatePassword(self, password):
        return generate_password_hash(password)
  
    def get_by_email(correo: str):
        sql = f"SELECT * FROM usuarios WHERE correo = '{correo}'"
        cursor.execute(sql)
        user_data = cursor.fetchone()
        print(user_data[0])
        if user_data:
            return User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
        else:
            return None
    
    def get_id(self):
        return str(self.id)
    
    def get(user_id):
        sql = f"SELECT * FROM usuarios WHERE id_usuario = {user_id}"
        cursor.execute(sql)
        user_data = cursor.fetchone()
        print(user_data)
        if user_data:
            return User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
        else:
            return None
