# -*- coding: utf-8 -*-

'''
Created on 2013年11月15日

@author: liufang.deng
'''

from o2olib import logger
import httplib2 as http
import json
from o2olib.QException import QException
from urllib import urlencode
from o2olib.login.LoginService import LoginService

API_URL = "https://api.weibo.com/2/users/show.json"  

class SinaLoginService(LoginService):

    def build_guest(self,args):
        guest = {}
        guest["weibo_uid"] = args.get("userId")
        return guest
    
    def get_guest(self,args):
        access_token = args.get("token")
        uid = args.get("userId")
        
        h = http.Http(".cache")
        url = "%s?%s"%(API_URL,urlencode({"access_token": access_token,"uid":uid}))
    
        r, content = h.request(url,"GET")
        ret_data = json.loads(content)
        
        logger.debug(u"login_from_sina,url:%s ret_data:%s"%(url,ret_data))
        
        if ret_data.get("error_code"):
            raise QException(u"获取用户信息失败")
        
        name = ret_data.get("name")
        weibo_uid = ret_data.get("idstr")
        gender = ret_data.get("gender")
        guest = {
                 "name": name
                 ,"weibo": name
                 ,"weibo_uid": weibo_uid
                 ,"gender": gender
                 }
        return guest
    
