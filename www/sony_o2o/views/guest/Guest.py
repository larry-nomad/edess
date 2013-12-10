# -*- coding: utf-8 -*-

from flask import request, session
from o2olib import GuestService
from Resource import Resource
from o2olib.utils import utils
from sony_o2o.libs.auth import require_login
from flask.ext.restful import reqparse
from o2olib.utils import typesChecker as tc 
from o2olib import logger

class Guest(Resource):
    
    def __init__(self): 

        self.parser_update = reqparse.RequestParser()
        self.parser_update.add_argument('id', type=tc.check_int, help=u'用户id错误')
        self.parser_update.add_argument('name', type=tc.check_str_required, help=u'登录名称必须填写')
        self.parser_update.add_argument('email', default=None,type=tc.check_email, help=u'请填写正确的email地址')
        self.parser_update.add_argument('gender', choices=[u"f",u"m"], type=str, help=u'请选择正确的性别')
        self.parser_update.add_argument('birthday', default=None, type=tc.check_date, help=u'请输入正确的生日,应为“YYYY年MM月DD日”或“YYYY-MM-DD”')
        self.parser_update.add_argument('telephone', default=None, type=tc.check_int, help=u'请输入正确的手机号码')
        self.parser_update.add_argument('qq', default=None, type=tc.check_int, help=u'请输入正确的QQ号码')
        self.parser_update.add_argument('wechat', default=None, type=tc.check_str, help=u'请输入正确的微信号码')
        self.parser_update.add_argument('weibo', default=None, type=tc.check_str,help=u'请输入正确的微博')
        super(Guest, self).__init__()

    @require_login
    def get(self):
        return GuestService.get(session["guest_id"])

    def post(self):
        args = self.parser_update.parse_args()
        guest = utils.multidict2dict(request.form)
        return GuestService.add(guest)
    
    @require_login
    def put(self):
        guest = self.parser_update.parse_args()
#         guest = utils.multidict2dict(request.form)
        guest["id"] = session["guest_id"]
        return GuestService.update(guest)
    
    def delete(self,id):
        if id:
            return GuestService.delete(id)

class Guests(Resource):

#     @require_login
    def get(self):
        con_dic = utils.multidict2dict(request.args)
        return GuestService.gets(con_dic)
#         return []
