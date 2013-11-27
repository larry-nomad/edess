# -*- coding: utf-8 -*-

'''
Created on 2013年11月15日

@author: liufang.deng
'''

from o2olib.login.SinaLoginService import SinaLoginService
from o2olib.login.QQLoginService import QQLoginService
from o2olib import logger
from flask import redirect,Blueprint,request,session
from o2olib.QException import QException
import re

BP = Blueprint('login', __name__)

def loginServiceFactory(domain):
    logger.debug("login,domain:%s"%domain)
    
    if domain and re.search("sina", domain, re.IGNORECASE):
        return SinaLoginService()
    elif domain and re.search("qq", domain, re.IGNORECASE):
        return QQLoginService()
    else:
        raise QException(u"不支持这种登陆方式，domain:%s"%domain)

@BP.route("v1/login")     
def login():
    domain = request.args.get("domain")
    guest = loginServiceFactory(domain).login(request.args)
    session["guest_id"] = guest.get("id")
    session["guest_name"] = guest.get("name")
    return redirect(request.args.get("ret"))    
    
@BP.route("v1/logout")
def logout():
    session.pop("guest_id",None)
    session.pop("guest_name",None)
    return redirect('/')
