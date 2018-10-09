from Flask import request, redirect, url_for, current_app, Response, g
from user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature



class Auth():
    def authenticate(self, username, password):
        pass
    def identity(self, payload):
        pass

def _auth_required():

    token = request.headers.get('Authorization')
    
    if token:
        if "access" in token:
            token_type = "access"
            expires_in = current_app.config['ACCESS_TOKEN_EXPIRE_TIME']
        elif "refresh" in token:
            token_type = "refresh"
            expires_in = current_app.config['REFRESH_TOKEN_EXPIRE_TIME']

        s = Serializer(
            current_app.config['SECRET_KEY'],
            expires_in = expires_in
        )
        try:
            data = s.loads(token)
            g.user = User(data.get("user_id"))

        except SignatureExpired:

            if token_type == "access":
                return Response()#valid access token
            elif token_type == "refresh":
                return redirect(url_for("signin"))

        except BadSignature:
            return redirect(url_for("error", error_value="Not A Verified User"))

        except NameError:
            return redirect(url_for("error", error_value="Not A Valid User"))

    else:
        return redirect(url_for("signin"))


def auth_required(fn):
    def replacement(*args, **kwargs):
        _auth_required()
        return fn(*args, **kwargs)
    return replacement
    