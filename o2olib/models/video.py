# -*- coding: utf-8 -*-

from modelbase import ModelBase
from o2olib.models.product import ProductModel
from o2olib.peewee import *

class VideoModel(ModelBase):
    class Meta:
        db_table = 'map_product_video'
    id = IntegerField()
    product_id = ForeignKeyField(ProductModel,db_column = "product_id")#IntegerField()
    video_url = CharField()
    description = TextField()
