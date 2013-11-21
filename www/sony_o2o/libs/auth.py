# -*- coding: utf-8 -*-

from functools import wraps
from flask import Response, redirect,session, request
from o2olib import logger
from o2olib.QException import QException
from JsonResult import JsonResult as JR
import json



LOGIN_URL = "http://oauth.qunar.com/oauth-client/%s/login?appname=%s&display=mobile&ret=%s&method=login&vistor=%s"%(
                "qq"#"sina"
                 ,"www"
                 ,"http://lfd.qunar.com:8888/hot"
                 ,"http://lfd.qunar.com:8888/v1/login")
                 

def check_user():
    if "guest_id" in session:
        logger.debug("check_user:guest:%s"%session["guest_id"])
        return True
    return False

def authenticate():
#     jr = JR().set_error_msg(u"请登录").to_dic()
    raise QException(u"请登录")
#     return redirect(LOGIN_URL)

def require_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not check_user():
            return authenticate()
        rs = f(*args, **kwargs)
        return rs
    return decorated


class require_post_field(object):
    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, func):
        def invoke(*args, **kwargs):
            if not self.field_name in request.form:
                raise QException(msg='not found key %s' % self.field_name)
            return func(*args, **kwargs)
        invoke.__name__ = func.__name__
        return invoke
