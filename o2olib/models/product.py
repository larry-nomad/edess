# -*- coding: utf-8 -*-

from modelbase import ModelBase
from o2olib.peewee import *


class ProductModel(ModelBase):
    class Meta:
        db_table = 'table_product'
    id = IntegerField()
    name = CharField()
    category = CharField()
    manufacturer = CharField()
    brief = TextField()
    invisible = BooleanField()

    
