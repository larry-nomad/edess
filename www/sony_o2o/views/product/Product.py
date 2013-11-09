# -*- coding: utf-8 -*-

from flask.ext import restful
from flask import request
from sony_o2o.libs import auth
from o2olib import ProductService
from o2olib import LikeService
from JsonResult import JsonResult 

class Product(restful.Resource):
    
    def get(self, id):
        product =  ProductService.get_product(id)
        if product:
            product["likesCount"] = LikeService.count_likes({"productId": product.get("id")})
        #return JsonResult(product)
        return product

class ProductList(restful.Resource):

    def get(self):
        invisibleStr = request.args.get("invisible")
        invisible = self.str2bool(invisibleStr)
        conDic = {
                "name": request.args.get("name"),
                "category": request.args.get("category"),
                "manufacturer": request.args.get("manufacturer"),
                "invisible": invisible
                }
        print conDic
        products = ProductService.get_products(conDic)
        for product in products:
            product["likeCount"] = LikeService.count_likes({"productId": product.get("id")})
        return products

    def str2bool(self,str):
        if not str:
            return None
        elif str.lower() in ("false","f","no"):
            return False
        else:
            return True
