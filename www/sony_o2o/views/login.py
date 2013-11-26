# -*- coding: utf-8 -*-

'''
Created on 2013年11月15日

@author: liufang.deng
'''

from o2olib import LoginService
from o2olib import logger
import re
from flask import redirect,Blueprint,request,session
from o2olib.QException import QException

BP = Blueprint('login', __name__)
LOGIN_URL = "http://oauth.qunar.com/oauth-client/%s/login?appname=%s&display=mobile&ret=%s&method=login&vistor=%s"
#                 %(
#                 "qq"#"sina"
#                  ,"www"
#                  ,"http://lfd.qunar.com:8888/hot"
#                  ,"http://lfd.qunar.com:8888/v1/login")
@BP.route("v1/dologin")
def do_login():
    domain = request.args.get("domain")
    ret = request.args.get("ret")
    logger.debug("request.url:%s request.base_url:%s request.url_root:%s request.host_url:%s"%(request.url,request.base_url,request.url_root,request.host_url))
    login_url = "%s/v1/login"%request.host_url
    url = LOGIN_URL%(domain,"www",ret,login_url)
    return redirect(url)
    
@BP.route("v1/login")     
def login():
    domain = request.args.get("domain")
    logger.debug("login,domain:%s"%domain)
    guest = None
    if domain and re.search("sina", domain, re.IGNORECASE):
        guest = LoginService.login_from_sina(request.args)
    elif domain and re.search("qq", domain, re.IGNORECASE):
        guest = LoginService.login_from_qq(request.args)
    else:
        raise QException(u"不支持这种登陆方式，domain:%s"%domain)
        
    session["guest_id"] = guest.get("id")
    session["guest_name"] = guest.get("name")
#     session.save()
    ret = request.args.get("ret")
    logger.debug("login,guest:%s ret:%s"%(session["guest_id"],ret))
#     return render_template("index.html#", data = guest)
    return redirect(ret)    
    
@BP.route("v1/logout")
def logout():
    session.pop("guest_id",None)
    session.pop("guest_name",None)
    return redirect('/')
