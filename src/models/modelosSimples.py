from databases.conexion import getConecction



def getPrograms():
    
    mybd = getConecction()
    cursor = mybd.cursor()
    
    sql = "select programa  from programas"
    cursor.execute(sql)
    programas = cursor.fetchall()
    print(list(programas))
    return programas


def getTipoDocumento():
    mybd = getConecction()
    cursor = mybd.cursor()
 
    sql="select tipo_documento from tipos_documento"
    cursor.execute(sql)
    tiposDocumento = cursor.fetchall()
    return tiposDocumento

def getSedes():
    mybd = getConecction()
    cursor = mybd.cursor()
 
    sql="select sede from sedes"
    cursor.execute(sql)
    sedes = cursor.fetchall()
    return sedes


def getMaterias():
    mybd = getConecction()
    cursor = mybd.cursor()
 
    sql="select materia from materias"
    cursor.execute(sql)
    materias = cursor.fetchall()
    return materias


def getSalon():
    mybd = getConecction()
    cursor = mybd.cursor()
 
    sql="select salon from salones"
    cursor.execute(sql)
    materias = cursor.fetchall()
    return materias

def getEstadoTutoria():
    mybd = getConecction()
    cursor = mybd.cursor()
 
    sql="select estado_tutoria from estados_tutorias"
    cursor.execute(sql)
    estado = cursor.fetchall()
    return estado


def existEmail(email:str):
    mybd = getConecction()
    cursor = mybd.cursor()
 
    sql=f'select count(*) from usuarios u  where u.correo="{email}" '
    cursor.execute(sql)
    existe = cursor.fetchone()[0]
    return existe

def existNumeroDocumento(numeroDocumento:str):
    mybd = getConecction()
    cursor = mybd.cursor()
 
    sql=f'select count(*) from estudiantes u  where u.numero_documento="{numeroDocumento}" '
    cursor.execute(sql)
    existe = cursor.fetchone()[0]
    return existe

def getFacultades():
    mybd = getConecction()
    cursor = mybd.cursor()
 
    sql="select facultad from facultades"
    cursor.execute(sql)
    estado = cursor.fetchall()
    return estado