# -*- coding: utf-8 -*-

from flask.ext import restful
from JsonResult import JsonResult
from o2olib import logger

def wrap_result(func):
    @restful.wraps(func)
    def wrapper(*args,**kwargs):
        rs = func(*args,**kwargs)
        logger.debug("wrap_result.wrapper，rs:%s"%rs)
        return JsonResult(rs).to_dic()
    return wrapper

class Resource(restful.Resource):
    method_decorators = [wrap_result]


