# -*- coding: utf-8 -*-

from flask import request
from o2olib import ProductService
from o2olib import LikeService
from o2olib import ReviewService
from o2olib import ManualService
from o2olib import GuestService
from Resource import Resource
from o2olib.utils import utils


def fill_product(product):
    if product:
        con = { "product_id": product.get("id")}
        product["likes_count"] = LikeService.count_likes(con)
        product["starts_counts"] =  ReviewService.count_stars(con)

class Product(Resource):
    
    def get(self, id):
        product =  ProductService.get(id)
        fill_product(product)
        return product

class Products(Resource):

    def get(self):
        con_dic = utils.multidict2dict(request.args)
        products = ProductService.gets(con_dic)
        for product in products:
            fill_product(product)
        return products

class Review(Resource):
    def post(self):
        review = utils.multidict2dict(request.form)
        review["id"] = None
        review["is_approved"] = False
        return ReviewService.add(review)

    #auth
    def put(self):
        review = utils.multidict2dict(request.form)
        #review["guest_id"] = session.get[""]
        return ReviewService.update(review)
    
    #auth
    def delete(self,id):
        obj = {"id":id}
        obj["guest_id"] = 14
        return ReviewService.delete(obj)
        

class Reviews(Resource):
    def get(self):
        con_dic = utils.multidict2dict(request.args)
        reviews = ReviewService.gets(con_dic)
        for review in reviews:
            review["guest"] = GuestService.get(review.get("guest"))
        return reviews

class ReviewsForGuest(Resource):
    def get(self):
        con_dic =utils.multidict2dict(request.args)
        con_dic["guest_id"] = 16
        reviews = ReviewService.get_reviews_for_guest(con_dic)
        return reviews


class Like(Resource):
    #@auth.require_login()
    def post(self):
        like = utils.multidict2dict(request.form)
        #like["guest_id"] = 1
        '''
        session['guestId']
        '''
        return  LikeService.add(like)
    
    #@auth.require_login()    
    def delete(self):
        like =  utils.multidict2dict(request.args)
        #like["id"] = id
        '''
        like["productId"] = request.form['productId']
        like["guestId"] = 1
        session['guestId']
        '''
        return LikeService.delete(like)

class Likes(Resource):
    def get(self):
        con = utils.multidict2dict(request.args)
        con["guest_id"] = 14
        return ProductService.get_products_for_like(con)

class Manual(Resource):
    #@auth.require_login()
    def post(self):
        obj = utils.multidict2dict(request.form)
        #like["guest_id"] = 1
        '''
        session['guestId']
        '''
        return  ManualService.add(obj)
    
    #@auth.require_login()    
    def delete(self):
        obj =  utils.multidict2dict(request.args)
        #obj["id"] = id
        return ManualService.delete(obj)

class Manuals(Resource):
    def get(self):
        con = utils.multidict2dict(request.args)
        con["guest_id"] = 14
        return ProductService.get_products_for_manual(con)
