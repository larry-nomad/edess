# -*- coding: utf-8 -*-

'''
Created on 2013年11月19日

@author: liufang.deng
'''
from functools import wraps
from flask import Response, redirect,session
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

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not check_user():
            return authenticate()
        rs = f(*args, **kwargs)
        return rs
    return decorated