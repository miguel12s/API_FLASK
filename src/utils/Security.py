import datetime
import pytz
import jwt
class Security():
    tz=pytz.timezone("America/Bogota")

    @classmethod
    def generateToken(cls,id_usuario):
        payload={
            'iat':datetime.datetime.now(tz=cls.tz),
            'exp':datetime.datetime.now(tz=cls.tz)+datetime.timedelta(minutes=10),
            'id_usuario':id_usuario,
            

        }
        return jwt.encode(payload,"secret_key",algorithm="HS256")
    @classmethod
    def verify_token(cls,headers):
        if 'Authorization'in headers.keys():
         authorization=headers['Authorization']
         token=authorization.split(' ')[1]
         try:
            payload=jwt.decode(token,'secret_key',algorithms='HS256')
            return payload
         except (jwt.ExpiredSignatureError,jwt.ExpiredSignatureError):
            return False
        return False


            
            