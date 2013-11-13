# -*- coding: utf-8 -*-

from flask.ext import restful
from flask import request
from sony_o2o.libs import auth
from o2olib import GuestService
from JsonResult import JsonResult as JR


class Guest(restful.Resource):

    #@auth.require_login()
    def get(self, id):
        guests = GuestService.get_guests()
        if len(guests) == 0:
            rs = {}
        else:
            rs = guests[0]
        return JR(rs).to_dic()

    def post(self):
        guest = dict(request.form)
        rs = GuestService.add_guest(guest)
        return JR(rs).to_dic()

    def put(self):
        guest = dict(request.form)
        rs = GuestService.update_guest(guest)
        return JR(rs).to_dic()

    def delete(self,id):
        if id:
           rs = GuestService.delete_guest(id)
        return JR(rs).to_dic()

class GuestList(restful.Resource):

    #@auth.require_login()
    def get(self):
        con_dic = dict(request.args)
        return GuestService.get_guests(con_dic)
