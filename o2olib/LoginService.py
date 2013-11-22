# -*- coding: utf-8 -*-

'''
Created on 2013年11月15日

@author: liufang.deng
'''

from o2olib import GuestService
from o2olib import logger
import httplib2 as http
import json
from o2olib.QException import QException
from datetime import datetime
from urllib import urlencode

SINA_API_URL = "https://api.weibo.com/2/users/show.json"  
QQ_API_URL = "https://graph.qq.com/user/get_user_info"
OPEN_ID_GETTER_URL = "https://graph.z.qq.com/moc2/me"
GENDER_DICT_FOR_QQ = {u"男":"m", u"女":"f"}

def login_from_sina(args):
    access_token = args.get("token")
    uid = args.get("userId")
    
    h = http.Http(".cache")
#     url = urlencode("%s?access_token=%s&uid=%s"%(SINA_API_URL,access_token,uid))
    url = "%s?%s"%(SINA_API_URL,urlencode({"access_token": access_token,
                                         "uid":uid}))

    r, content = h.request(url,"GET")
    ret_data = json.loads(content)
    logger.info(u"login_from_sina,url:%s ret_data:%s"%(url,ret_data))
    if ret_data.get("error_code"):
        raise QException(u"获取用户信息失败")
    
    name = ret_data.get("name")
    weibo = ret_data.get("idstr")
    gender = ret_data.get("gender")
    guest = {
             "name": name
             ,"weibo": weibo
             ,"gender": gender
             }
    return login(guest)

def login_from_qq(args):
    access_token = args.get("token")
    rs = get_open_id(access_token)
    openid = rs.get("qq_openid")
    appid = rs.get("appid")
    h = http.Http(".cache")
#     url = "%s?%s"%(QQ_API_URL,urlencode("oauth_consumer_key=%s&access_token=%s&openid=%s&format=%s"%(appid,access_token,openid,"json")))

    url = "%s?%s"%(QQ_API_URL,urlencode({"oauth_consumer_key": appid,
                                         "access_token":access_token,
                                         "openid":openid,
                                         "format":json}))
    r,content = h.request(url,"GET")
    ret_data = json.loads(content) 
    logger.info(u"login_from_qq,url:%s ret_data:%s"%(url,ret_data))
    if ret_data.get("ret") != 0:
        raise QException(u"获取用户信息失败")
    
    name = ret_data.get("nickname")
    qq = ret_data.get("nickname")
    gender = ret_data.get("gender")
    return login({
                  "qq_openid":openid
                  ,"qq":qq
                  ,"name":name
                  ,"gender":GENDER_DICT_FOR_QQ.get(gender)
                  })
    

def get_open_id(token):
    h = http.Http(".cache")
    url = "%s?access_token=%s"%(OPEN_ID_GETTER_URL,token)
    resp, content = h.request(url,"GET")
    contents = content.split("&")
    rs = {}
    cs = contents[0].split("=")
    rs["appid"] = cs[1]
    cs = contents[1].split("=")
    rs["qq_openid"] = cs[1]
         
    return rs

def login(guest):
    guests = GuestService.gets(guest)
    if len(guests) == 0:
        guest["register_date"] = datetime.now()
        guest["last_active_date"] = datetime.now()
        guest["id"] = GuestService.add(guest)
    else:
        guest = guests[0]
        guest["last_active_date"] = datetime.now()
        GuestService.update(guest)
    return guest

