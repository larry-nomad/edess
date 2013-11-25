# -*- coding: utf-8 -*-

from flask import request
from o2olib import GuestService
from Resource import Resource
from o2olib.utils import utils
from sony_o2o.libs.auth import require_login
from flask.ext.restful import reqparse, types

class Guest(Resource):
    
    def __init__(self):

        self.parser_update = reqparse.RequestParser()
        self.parser_update.add_argument('id', type=int, dest='guest_id', required=False, help='用户id错误')
        self.parser_update.add_argument('name', required=True, help='称呼必须填写')
        self.parser_update.add_argument('email', type=GuestService.check_email, required=False, help='请填写正确的email地址')
        self.parser_update.add_argument('gender', type=str, help='请选择正确的性别')
        self.parser_update.add_argument('birthday', type=types.date, default='0000-00-00', help='请输入正确的生日')
        self.parser_update.add_argument('telephone', type=int, help='请输入正确的手机号码')
        self.parser_update.add_argument('qq', type=int, help='请输入正确的QQ号码')
        self.parser_update.add_argument('wechat', type=str, help='请输入正确的微信号码')
        self.parser_update.add_argument('weibo', type=str,help='请输入正确的微博')
        self.parser_update.add_argument('twitter', type=str, help='twitter error')
        self.parser_update.add_argument('facebook', type=str, help='facebook error')
        self.parser_update.add_argument('google_plus', type=str, help='google_plus error')
        self.parser_update.add_argument('alipay', type=str, help='alipay error')
        self.parser_update.add_argument('paypal', type=str, help='paypal error')
        self.parser_update.add_argument('credit_point', type=int, help='credit point error')
        self.parser_update.add_argument('influence_point', type=str, help='influence_point code error')

    @require_login
    def get(self, id):
        return GuestService.get(id)

    def post(self):
        args = self.parser_update.parse_args()
        guest = utils.multidict2dict(request.form)
        return GuestService.add(guest)
    
    def put(self):
        args = self.parser_update.parse_args()
        guest = utils.multidict2dict(request.form)
        return GuestService.update(guest)
    
    def delete(self,id):
        if id:
            return GuestService.delete(id)

class Guests(Resource):

    @require_login
    def get(self):
        con_dic = utils.multidict2dict(request.args)
        return GuestService.gets(con_dic)
