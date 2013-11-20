# -*- coding: utf-8 -*-

'''
Created on 2013年11月15日

@author: liufang.deng
'''

from o2olib import LoginService
from o2olib import logger
import re
from flask import redirect,Blueprint,request,session

BP = Blueprint('login', __name__)

API_URL = "https://api.weibo.com/2/users/show.json"  

@BP.route("v1/login")     
def login():
    domain = request.args.get("domain")
    logger.debug("login,domain:%s"%domain)
    guest = None
    if domain and re.search("sina", domain, re.IGNORECASE):
        guest = LoginService.login_from_sina(request.args)
    elif domain and re.search("qq", domain, re.IGNORECASE):
        guest = LoginService.login_from_qq(request.args)
        
    session["guest_id"] = guest.get("id")
    session["guest_name"] = guest.get("name")
    ret = request.args.get("ret")
    logger.debug("login,guest:%s ret:%s"%(session["guest_id"],ret))
    return redirect(ret)    
    
@BP.route("v1/logout")
def logout():
    session.pop("guest_id",None)
    session.pop("guest_name",None)
    return redirect('/hot')
