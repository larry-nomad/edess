# -*- coding: utf-8 -*-

from flask.ext import restful
from flask import request,session
from sony_o2o.libs import auth
from o2olib import LikeService

class Like(restful.Resource):
    #@auth.require_login()
    def post(self):
        productId = request.form['productId']
        like = {}
        like["guestId"] = 1
        '''
        session['guestId']
        '''
        like["productId"] = productId
        return  LikeService.add_like(like)
    
    #@auth.require_login()    
    def delete(self, id):
        like = {}
        like["id"] = id
        '''
        like["productId"] = request.form['productId']
        like["guestId"] = 1
        session['guestId']
        '''
        return LikeService.delete_like(like)
