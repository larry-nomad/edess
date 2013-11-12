# -*- coding: utf-8 -*-

from modelbase import ModelBase
from o2olib.models.product import ProductModel
from o2olib.peewee import *

class ManualModel(ModelBase):
    class Meta:
        db_table = 'map_guest_manuals'
    id = IntegerField()
    product = ForeignKeyField(ProductModel)#IntegerField()
    guest_id = IntegerField()
