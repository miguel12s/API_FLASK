from werkzeug.security import check_password_hash,generate_password_hash

class User:
    id_rol:int
    id_estado:int
    
    correo:str
    contraseña:str

    def __init__(self,id_rol,id_estado,correo,contraseña) -> None:
        self.id_rol=id_rol
        self.id_estado=id_estado
        self.correo=correo
        self.contraseña=generate_password_hash(contraseña)

    @classmethod    
    def checkPassword(self,passwordHashed,password):
       return  check_password_hash(passwordHashed,password)
