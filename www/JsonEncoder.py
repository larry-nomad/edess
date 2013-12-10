# -*- encoding:utf-8 -*-

 
import json
from datetime import datetime,date,time

class JsonEncoder(json.JSONEncoder):
    DATE_FORMAT = u"%Y年%m月%d日"
    TIME_FORMAT = u"%H时%M分%S秒"

    def default(self,obj):
        if isinstance(obj, datetime):
            return safeNewDatetime(obj).strftime("%s %s" % (self.DATE_FORMAT,self.TIME_FORMAT))
        if isinstance(obj, date):
            return safeNewDate(obj).strftime(self.DATE_FORMAT)
        if isinstance(obj, time):
            return obj.strftime(self.TIME_FORMAT)
        else:
            return  json.JSONEncoder.default(self, obj)


def safeNewDatetime(d):
    kw = [d.year, d.month, d.day]  
    if isinstance(d, datetime):  
        kw.extend([d.hour, d.minute, d.second, d.microsecond, d.tzinfo])  
    return datetime(*kw)  

def safeNewDate(d):  
    return date(d.year, d.month, d.day)

