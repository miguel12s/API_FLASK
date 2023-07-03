from databases.conexion import getConecction


mybd = getConecction()
cursor = mybd.cursor()


def getPrograms():
    
    sql = "select programa  from programas"
    cursor.execute(sql)
    programas = cursor.fetchall()
    print(list(programas))
    return programas


def getTipoDocumento():
    sql="select tipo_documento from tipos_documento"
    cursor.execute(sql)
    tiposDocumento = cursor.fetchall()
    return tiposDocumento
