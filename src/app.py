from flask import Flask, jsonify,request
from models.estudiante import Estudiante
from models.modelos import insertarUsuario
app=Flask(__name__)


@app.route('/')
def index():
       
    return jsonify('bienvenido')

@app.route('/registro',methods=['POST'])

def registro():
    response={}
    
    try:
        data:Estudiante=request.json
        print(data['nombre'])
        if not data:
            response={'message':'no hay datos en la request'}
            status=400
        return jsonify(response,status,data)

            
    except Exception as e:
        response={'message':'solicitud procesada'}
        status=200
        insertarUsuario(data)

        return jsonify(response,status,data)
       
   
    

if __name__=='__main__':
    app.run(debug=True)
