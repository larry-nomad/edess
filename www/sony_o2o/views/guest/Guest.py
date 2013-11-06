# -*- coding: utf-8 -*-

from flask.ext import restful
from flask import request
from sony_o2o.libs import auth
from o2olib import GuestService


class Guest(restful.Resource):

    #@auth.require_login()
    def get(self, id):
        guest = {"id": id}
        return guest

    def post(self):
        guest = {"name": 'luyan'}
        GuestService.add_guest(guest)
        return guest

    def put(self, id):
        guest = {}
        guest['id'] = id
        guest['name'] = request.form.get('name')
        GuestService.update_guest(guest)
        return guest

    def delete(self):
        GuestService.delete_guest(id)
        return id


class GuestList(restful.Resource):

    #@auth.require_login()
    def get(self):
        print 'you search me'
        print request.args.get('name')
        return ''
