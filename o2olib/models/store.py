# -*- coding: utf-8 -*-

from modelbase import ModelBase
from o2olib.peewee import IntegerField, CharField, TextField


class StoreModel(ModelBase):
    class Meta:
        db_table = 'dict_sony_store'
    id = IntegerField()
    name = CharField()
    address = CharField()
    gps_location = CharField()
    telephone = TextField()
    
