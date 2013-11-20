# -*- coding: utf-8 -*-

from flask import request,session
from o2olib import ProductService
from o2olib import LikeService
from o2olib import ReviewService
from o2olib import ManualService
from o2olib import GuestService
from Resource import Resource
from o2olib.utils import utils
from auth import requires_auth as auth


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

    @auth
    def put(self):
        review = utils.multidict2dict(request.form)
        review["guest_id"] = session["guest_id"]
        return ReviewService.update(review)
    
    @auth
    def delete(self,id):
        obj = {"id":id}
        obj["guest_id"] = session["guest_id"]
        return ReviewService.delete(obj)
        

class Reviews(Resource):
    
    @auth
    def get(self):
        con_dic = utils.multidict2dict(request.args)
        con_dic["guest_id"] = session["guest_id"]
        reviews = ReviewService.gets(con_dic)
        for review in reviews:
            review["guest"] = GuestService.get(review.get("guest_id"))
        return reviews

class ReviewsForGuest(Resource):
    
    @auth
    def get(self):
        con_dic =utils.multidict2dict(request.args)
        con_dic["guest_id"] = session["guest_id"]
        reviews = ReviewService.get_reviews_for_guest(con_dic)
        return reviews


class Like(Resource):
    
    @auth
    def post(self):
        like = utils.multidict2dict(request.form)
        like["guest_id"] = session["guest_id"]
        return  LikeService.add(like)
    
    @auth
    def delete(self):
        like =  utils.multidict2dict(request.args)
        session["guest_id"] = session["guest_id"]
        return LikeService.delete(like)

class Likes(Resource):
    
    @auth
    def get(self):
        con = utils.multidict2dict(request.args)
        con["guest_id"] = session["guest_id"]
        return ProductService.get_products_for_like(con)

class Manual(Resource):
    
    @auth
    def post(self):
        obj = utils.multidict2dict(request.form)
        obj["guest_id"] = session["guest_id"]
        return  ManualService.add(obj)
    
    @auth
    def delete(self):
        obj =  utils.multidict2dict(request.args)
        obj["guest_id"] = session["guest_id"]
        return ManualService.delete(obj)

class Manuals(Resource):
    
    @auth
    def get(self):
        con = utils.multidict2dict(request.args)
        con["guest_id"] = session["guest_id"]
        return ProductService.get_products_for_manual(con)
