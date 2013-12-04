# -*- coding: utf-8 -*-

'''
Created on 2013年12月4日

@author: liufang.deng
'''
from flask.ext.restful import types
from o2olib import logger
from datetime import datetime
import re
import six
from functools import wraps

"""
reqparse中没有将异常打印出来，不便跟踪问题，只有在这里打印异常了
"""
def do_check_log(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            rs = f(*args, **kwargs)
        except TypeError,te:
            raise te
        except Exception,e:
            logger.exception(e)
            raise e
        return rs
    return decorated

@do_check_log
def check_email(val,name):
    val = get_val(val)
    if not val:
        return val
    re_email = re.compile(r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}$', re.IGNORECASE)
    re_email_res = re_email.match(val)
    if not re_email_res:
        raise ValueError(u"邮件格式 ’{}’ 不正确".format(val))
    return val

@do_check_log
def check_date(val,name):
    val = get_val(val)
    if not val:
        return val
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

@do_check_log
def check_int(val,name):
    val = get_val(val)
    if not val:
        return val
    return int(val)

@do_check_log
def check_str(val,name):
    val = get_val(val)
    if not val:
        return val
    return six.text_type(val)

"""
check_str方法里异常会被打印两遍
"""
@do_check_log
def check_str_required(val,name):
    val = get_val(val)
    if not val:
        raise ValueError(u"val required")
    return check_str(val,name)

def get_val(val):
    if val == None:
        return None
    return val.strip(" ")
