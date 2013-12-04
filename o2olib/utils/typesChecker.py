# -*- coding: utf-8 -*-

'''
Created on 2013年12月4日

@author: liufang.deng
'''
from flask.ext.restful import types
from datetime import datetime
import re
from o2olib.QException import QException

def check_email(val,name):
    if not val:
        return None    
    'check email'
    re_email = re.compile(r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}$', re.IGNORECASE)
    re_email_res = re_email.match(val)
    if not re_email_res:
        raise ValueError(u"邮件格式 ’{}’ 不正确".format(val))
    return val

def check_date(val,name):
    if not val:
        return None 
    date = None
    try: 
        date = datetime.strptime(val, u"%Y年%m月%d日")
    except:
        try:
            date = datetime.strptime(val, "%Y-%m-%d")
        except:
            raise ValueError(u"日期格式不正确，应为“YYYY年MM月DD日”或“YYYY-MM-DD”")
    if date.year < 1900:
        raise ValueError(u"Year must be >= 1900")
    return date  

def check_int(val,name):
    if not val:
        return None    
    return int(val)

def check_str(val,name):
    if not val:
        return None    
    return str(val)
