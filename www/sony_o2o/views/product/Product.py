# -*- coding: utf-8 -*-

from flask.ext import restful
from flask import request
from o2olib import ProductService
from o2olib import LikeService
from o2olib import ReviewService
from o2olib import ManualService
from JsonResult import JsonResult as JR

def fill_product(product):
    if product:
        con = { "product_id": product.get("id")}
        product["likes_count"] = LikeService.count_likes(con)
        product["starts_counts"] =  ReviewService.count_stars(con)

def str2bool(str):
    if not str:
        return None
    elif str.lower() in ("false","f","no"):
        return False
    else:
        return True

def request_to_dic(req):
    vs = req
    kvs = {}
    for k,v in vs.items():
        kvs[k] = req.get(k)
    return kvs


class Product(restful.Resource):
    
    def get(self, id):
        product =  ProductService.get_product(id)
        fill_product(product)
        return JR(product).to_dic()

class ProductList(restful.Resource):

    def get(self):
        con_dic = request_to_dic(request.args)
        products = ProductService.get_products(con_dic)
        for product in products:
            fill_product(product)
        return JR(products).to_dic()

class Review(restful.Resource):
    def post(self):
        review = request_to_dic(request.form)
        review["id"] = None
        review["is_approved"] = False
        return ReviewService.add_review(review)

    def put(self):
        review = requst_to_dic(request.form)
        return ReviewService.update_review(review)
    
    def delete(self,id):
        return ReviewService.delete_review(id)
        

class Reviews(restful.Resource):
    def get(self):
        is_approved_str = request.args.get("is_approvedStr")
        con_dic = request_to_dic(request.args)
        reviews = ReviewService.get_reviews(con_dic)
        return JR(reviews).to_dic()

class Like(restful.Resource):
    #@auth.require_login()
    def post(self):
        like = request_to_dic(request.form)
        #like["guest_id"] = 1
        '''
        session['guestId']
        '''
        return  LikeService.add_like(like)
    
    #@auth.require_login()    
    def delete(self, id):
        like =  request_to_dic(request.form)
        like["id"] = id
        '''
        like["productId"] = request.form['productId']
        like["guestId"] = 1
        session['guestId']
        '''
        return LikeService.delete_like(like)

class Manual(restful.Resource):
    #@auth.require_login()
    def post(self):
        obj = request_to_dic(request.form)
        #like["guest_id"] = 1
        '''
        session['guestId']
        '''
        return  ManualService.add(obj)
    
    #@auth.require_login()    
    def delete(self, id):
        obj =  request_to_dic(request.args)
        obj["id"] = id
        return ManualService.delete(obj)

class Manuals(restful.Resource):
    def get(self):
        con = {"guest_id":1}
        return JR(ProductService.get_products_for_manual(con)).to_dic()
