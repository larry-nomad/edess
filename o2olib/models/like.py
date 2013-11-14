# -*- coding: utf-8 -*-

from modelbase import ModelBase
from o2olib.models.product import ProductModel
from o2olib.peewee import *

class LikeModel(ModelBase):
    class Meta:
        db_table = 'map_guest_likes'
    id = IntegerField()
    product_id = ForeignKeyField(ProductModel,db_column = "product_id")#IntegerField()
    guest_id = IntegerField()
    like_date = DateTimeField()
