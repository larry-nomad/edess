# -*- coding: utf-8 -*-

from flask.ext import restful


#TODO 需要验证用户身份才能返回所有用户列表
class Guest(restful.Resource):
    def get(self):
        guest = {}
        return guest

    def post(self):
        guest = {}
        return guest
