from flask import Blueprint
from flask import request
import hashlib

BP = Blueprint('weixin', __name__)


@BP.route('weixin')
def weixin():
    if 'signature' in request.args and \
            'timestamp' in request.args and \
            'nonce' in request.args and \
            'echostr' in request.args:
        signature = request.args.get("signature")
        timestamp = request.args.get("timestamp")
        nonce = request.args.get("nonce")
        echostr = request.args.get("echostr")
        token = '9d3e73a365e1c8c5479ac0d1a341f15d'
        tmp_arrary = [
            token,
            timestamp,
            nonce
        ]
        tmp_arrary.sort()
        tmp_string = ''.join(tmp_arrary)
        tmp_string = hashlib.sha1(tmp_string).hexdigest()

        if tmp_string == signature:
            return echostr
        else:
            return tmp_string
    else:
        return 'bad parameters'
