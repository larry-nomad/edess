# -*- coding: utf-8 -*-

from flask import request, session
from sony_o2o.libs.ajax import *
from flask import Response
from sony_o2o.libs import ajax


# @decorator
class require_login(object):
    def __init__(self):
        pass

    def __call__(self, func):
        def invoke(*args, **kwargs):
            if not "guest_id" in session:
                return Response(ajax.ajax_error('require login'), status=401, mimetype='application/json')
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
