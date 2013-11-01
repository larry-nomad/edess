# -*- coding: utf-8 -*-

from flask.ext import restful

from opsapi_auth.libs import rest
from opsapi_auth.views.v1.error_info import error_code
from opsapi_auth.views.v1.error_info import error_msg
from opsapi_auth_lib.v1.service import auth_service


class TokenName(restful.Resource):
    def get(self, token_name):
        res = {
            'data': auth_service.GetTokenInfoByTokenName(token_name)
        }
        if res['data']:
            return rest.success(msg=error_msg.OBTAIN_TOKEN_INFO_SUCCEED_MSG, **res)
        else:
            return rest.error(errcode=error_code.NO_SUCH_TOKEN, msg=error_msg.NO_SUCH_TOKEN_MSG)
