# Online Python - IDE, Editor, Compiler, Interpreter
import base64
import hmac
from hashlib import sha256

def sign_request():
    signData = '$'.join(['POST', '/openapi/inventory/v1/sku/list']) + '$'
    ACCESS_KEY = 'd20254aee13cc156'
    SECRET_KEY = 'b3436f168a4402b7'
    authorization = ACCESS_KEY + ':' + base64.b64encode(
        hmac.new(SECRET_KEY.encode('utf-8'), signData.encode('utf-8'),digestmod=sha256).digest()).decode('ascii')
    return authorization

print(f'{sign_request()}')