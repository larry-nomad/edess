# -*- coding: utf-8 -*-

'''
Created on 2013年11月20日

@author: liufang.deng
'''
from modelbase import ModelBase
from product import ProductModel
from o2olib.peewee import IntegerField, CharField, ForeignKeyField

class ProductImgModel(ModelBase):
    class Meta:
        db_table = 'map_product_img'
    id = IntegerField()
    product_id = ForeignKeyField(ProductModel,db_column = "product_id",related_name = "imgs")
    small = CharField()
    medium = CharField()
    large = CharField()
    

