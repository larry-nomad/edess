# -*- coding: utf-8 -*-

import md5
from flask import request, session
from sony_o2o.libs.ajax import *
import settings
from sony_o2o import logger
from flask import Response
from sony_o2o.libs import ajax


# @decorator
class require_login(object):
    def __init__(self):
        pass

    def __call__(self, func):
        def invoke(*args, **kwargs):
            if request.authorization is not None:
                username = request.authorization['username']
                password = request.authorization['password']
                password = md5.new(password).hexdigest()
                check_client = clientLogin(username, password)
                if request.remote_addr not in settings.API_ALLOW_LIST:
                    logger.error('api ip %s is not in allow list.' % request.remote_addr)
                    return Response(ajax.ajax_error('require authorization'), status=401, mimetype='application/json')
                if check_client is True:
                    session['user_id'] = username
                    return func(*args, **kwargs)
                else:
                    return Response(ajax.ajax_error('require authorization'), status=401, mimetype='application/json')
            if not "user_id" in session:
                return ajax_direct_login()
            return func(*args, **kwargs)

        invoke.__name__ = func.__name__
        return invoke


# @decorator
class require_post_field(object):
    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, func):
        def invoke(*args, **kwargs):
            if not self.field_name in request.form:
                return ajax_error(msg='not found key %s' % self.field_name)
            return func(*args, **kwargs)
        invoke.__name__ = func.__name__
        return invoke
