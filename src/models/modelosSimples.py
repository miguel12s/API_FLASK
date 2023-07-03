from databases.conexion import getConecction


mybd = getConecction()
cursor = mybd.cursor()


def getPrograms():
    sql = "select * from programas"
    cursor.execute(sql)
    programas = cursor.fetchall()
    return programas


def getTipoDocumento():
    sql="select * from tipos_documento"
    cursor.execute(sql)
    tiposDocumento = cursor.fetchall()
    return tiposDocumento
