# -*- coding: utf-8 -*-

from flask.ext import restful
from sony_o2o.libs import auth


class Guest(restful.Resource):

    @auth.require_login()
    def get(self, id):
        guest = {"id": id}
        return guest

    def post(self):
        guest = {}
        return guest
