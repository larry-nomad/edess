# -*- coding: utf-8 -*-

from flask.ext import restful
from JsonResult import JsonResult

def wrap_result(func):
    @restful.wraps(func)
    def wrapper(*args,**kwargs):
        rs = func(*args,**kwargs)
        return JsonResult(rs).to_dic()
    return wrapper

class Resource(restful.Resource):
    method_decorators = [wrap_result]


