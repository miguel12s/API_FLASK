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
        self.correo=correo,
       
