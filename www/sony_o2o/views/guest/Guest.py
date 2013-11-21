# -*- coding: utf-8 -*-

from flask import request
from o2olib import GuestService
from Resource import Resource
from o2olib.utils import utils
from sony_o2o.libs.auth import require_login

class Guest(Resource):

    @require_login
    def get(self, id):
        return GuestService.get(id)

    def post(self):
        guest = utils.multidict2dict(request.form)
        return GuestService.add(guest)
    
    def put(self):
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
