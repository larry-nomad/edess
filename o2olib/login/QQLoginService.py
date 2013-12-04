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

API_URL = "https://graph.qq.com/user/get_user_info"
OPEN_ID_GETTER_URL = "https://graph.z.qq.com/moc2/me"
GENDER_DICT = {u"男":"m", u"女":"f"}

class QQLoginService(LoginService):

    def build_guest(self,args):
        access_token = args.get("token")
        me = self.get_openid_and_appid(access_token)
        guest = {}
        guest["qq_openid"] = me.get("openid")
        return guest
    
    def get_guest(self,args):
        access_token = args.get("token")
        me = self.get_openid_and_appid(access_token)
        openid = me.get("openid")
        appid = me.get("client_id")
        h = http.Http(".cache")
        url = "%s?%s"%(API_URL,urlencode({"oauth_consumer_key": appid,
                                             "access_token":access_token,
                                             "openid":openid,
                                             "format":json}))
        r,content = h.request(url,"GET")
        ret_data = json.loads(content) 
        logger.info(u"login_from_qq,url:%s ret_data:%s"%(url,ret_data))
        if ret_data.get("ret") != 0:
            raise QException(u"获取用户信息失败")
        
        name = ret_data.get("nickname")
#         qq = ret_data.get("nickname")
        gender = ret_data.get("gender")
        return {
                  "qq_openid":openid
#                   ,"qq":qq
                  ,"name":name
                  ,"gender":GENDER_DICT.get(gender)
                  }
        
    
    def get_openid_and_appid(self,token):
        h = http.Http(".cache")
        url = "%s?access_token=%s"%(OPEN_ID_GETTER_URL,token)
        r, content = h.request(url,"GET")
        logger.info(u"get_openid_and_appid,url:%s ret_data:%s"%(url,content))
        """
        ret_data格式:client_id=100244931&openid=FEBD4A0F4EE4A7A5EEC6B2BB04E766E1
        """
        contents = content.split("&")
        rs = {}
        for content in contents:
            kv = content.split("=")
            rs[kv[0]] = kv[1]
             
        return rs

