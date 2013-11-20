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

SINA_API_URL = "https://api.weibo.com/2/users/show.json"  
QQ_API_URL = "https://graph.qq.com/user/get_user_info"
OPEN_ID_GETTER_URL = "https://graph.z.qq.com/moc2/me"

def login_from_sina(args):
    access_token = args.get("token")
    uid = args.get("userId")
    
    h = http.Http(".cache")
    url = "%s?access_token=%s&uid=%s"%(SINA_API_URL,access_token,uid)
    r, content = h.request(url,"GET")
    ret_data = json.loads(content)
    logger.info("login_from_qq,url:%s ret_data:%s"%(url,content))
    if not ret_data.get("ret"):
        raise QException(u"获取用户信息失败")
    
    name = ret_data.get("name")
    weibo = ret_data.get("idstr")
    guest = {"name":name,"weibo":weibo}
    return login(guest)

def login_from_qq(args):
    access_token = args.get("token")
    rs = get_open_id(access_token)
    openid = rs.get("qq_openid")
    appid = rs.get("appid")
    h = http.Http(".cache")
    url = "%s?oauth_consumer_key=%s&access_token=%s&openid=%s&format=%s"%(QQ_API_URL,appid,access_token,openid,"json")
    r,content = h.request(url,"GET")
    ret_data = json.loads(content)
    logger.info("login_from_qq,url:%s ret_data:%s"%(url,content))
    if ret_data.get("ret") != 0:
        raise QException(u"获取用户信息失败")
    
    name = ret_data.get("nickname")
    qq = ret_data.get("nickname")
    return login({"qq_openid":openid,"qq":qq,"name":name})
    

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
        guest["id"] = GuestService.add(guest)
    else:
        guest = guests[0]
    return guest

