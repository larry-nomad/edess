# -*- coding: utf-8 -*-

import os
import random
import uuid
import decimal
from o2olib import logger
import datetime
from types import *
from time import sleep
from o2olib.QException import QException


def GenUuid():
    return unicode(uuid.uuid4())


def genUniqueCode(prefix=u"U"):
    result = u"%s%s%d"
    return result % (
        unicode(prefix),
        unicode(datetime.datetime.now().strftime("%Y%m%d%H%M%S")),
        random.randint(100000, 999999),
        )


# 尝试从(utf-8, gbk)转换成unicode
def covertUnicode(s, throw_exception=True):
    if isinstance(s, unicode):
        return s
    result = None
    is_succ = False
    if not is_succ:
        try:
            result = s.decode('utf-8')
            is_succ = True
        except:
            is_succ = False

    if not is_succ:
        try:
            result = s.decode('GBK')
            is_succ = True
        except:
            is_succ = False

    if is_succ:
        return result
    else:
        if throw_exception:
            raise ValueError("mast a UTF-8 or GBK str instance")
        else:
            return None


# 必须在程序开始调用
def setupLogger(dir_name, log_name):
    # check directories
    if not os.path.exists(dir_name):
        try:
            os.mkdir(dir_name)
        except Exception, _ex:
            print 'create dir error: %s' % str(_ex)
            return False
    if not os.path.isdir(dir_name):
        print '%s is not a directory.' % dir_name
        return False
    if not os.access(dir_name, os.R_OK | os.W_OK):
        print 'dir <%s> cannot access.' % dir_name
        return False

    # set logger
    logger.log_dir = dir_name
    logger.log_name = log_name
    logger.debug('logger [%s] initialized.', log_name)
    return True


def getPwMap(select_obj):
    result = []
    for item in select_obj:
        result.append(item.get_field_dict())
    return result


def device_striper(device):
    new_device = {}
    for key in device:
        if key is not None:
            if key not in ('remark') and type(device[key]) is UnicodeType:
                new_device[key] = device[key].strip()
            else:
                new_device[key] = device[key]
    return new_device


def jsonfy(mix):
    result = None
    if isinstance(mix, list):
        result = []
        for i in mix:
            result.append(jsonfy(i))
    elif isinstance(mix, dict):
        result = {}
        for k, v in mix.items():
            k = jsonfy(k)
            v = jsonfy(v)
            result[k] = v
    elif isinstance(mix, datetime.datetime):
        result = mix.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(mix, datetime.date):
        result = mix.strftime('%Y-%m-%d')
    elif isinstance(mix, decimal.Decimal):
        result = float(mix)
    else:
        return mix
    return result


def makeIndexedTable(table, map_key):
    result = {}
    for row in table:
        k = row[map_key]
        v = row
        result[k] = v
    return result


def mergeDuplicateRecord(result):
    hash_rlt = {}
    for i in result:
        hostname = i['host_name']
        service_description = i['service_description']
        unique_key = hostname + service_description
        v = i
        hash_rlt[unique_key] = v
    merge_rlt = []
    for i in hash_rlt:
        merge_rlt.append(hash_rlt[i])

    return merge_rlt


def is_valid(param):
        if(param is not None and param != '' and
                param != 'None'):
            return True
        else:
            return False


def RetryPoller(msg='', retry_times=3, interval=3):

    def Polling(func):
        poller_msg = msg if msg else func.__name__

        def DelegatePollerFunc(*args, **kwargs):
            current_retry_times = 0
            res = False
            while current_retry_times < retry_times:
                current_retry_times += 1
                try:
                    func(*args, **kwargs)
                except Exception, _ex:
                    logger.error('{msg} failed: Retry after {interval} second'
                                 '- Remain retry count {remain_times}'.format(
                                     msg=poller_msg,
                                     interval=interval,
                                     remain_times=(retry_times - current_retry_times)
                                     ))
                    logger.error(str(_ex))
                    sleep(interval)
                else:
                    res = True
                    break
            return res
        return DelegatePollerFunc
    return Polling

def str2bool(str):
    '''
    字符串转换成bool类型
    '''
    if not str:
        return None
    elif str.lower() in ("false","f","no"):
        return False
    else:
        return True

def multidict2dict(req):
    '''
    vs = req.to_dict(False)
    kvs = {}
    for k,v in vs.items():
        kvs[k] = req.get(k)
    return kvs
    '''
    return req.to_dict(False)

def get_val_from_dict(dict, key, type=None):
    if not dict or not key:
        raise QException(u"util.get_val_from_dict(dict:%s key:%s) dict,key都不能为空"%(dict,key))
    else:
        val = dict.get(key)
        if not val:
            return None
        if type:
            if not isinstance(val,list):
                return [val]
            else:
                return val
        else:
            if isinstance(val,list):
                return val[0]
            else:
                return val