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
            'id_usuario':id_usuario

        }
        return jwt.encode(payload,"secret",algorithm="HS256")