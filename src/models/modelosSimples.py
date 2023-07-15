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

def getSedes():
    sql="select sede from sedes"
    cursor.execute(sql)
    sedes = cursor.fetchall()
    return sedes


def getMaterias():
    sql="select materia from materias"
    cursor.execute(sql)
    materias = cursor.fetchall()
    return materias


def getSalon():
    sql="select salon from salones"
    cursor.execute(sql)
    materias = cursor.fetchall()
    return materias