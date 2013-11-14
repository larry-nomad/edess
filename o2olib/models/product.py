# -*- coding: utf-8 -*-

from modelbase import ModelBase
from o2olib.peewee import *
from o2olib.utils import utils


class ProductModel(ModelBase):
    class Meta:
        db_table = 'table_product'
    id = IntegerField()
    name = CharField()
    category = CharField()
    manufacturer = CharField()
    brief = TextField()
    invisible = BooleanField()

    @classmethod
    def build_con_dict(cls,con_dic):
        con = {}
        id = con_dic.get("id")
        if id:
            con["id"] = id

        name = con_dic.get("name")
        if name:
            con["name"] = "%%%s%%"%name

        category = con_dic.get("category")
        if category:
            con["category"] = category

        manufacturer = con_dic.get("manufacturer")
        if manufacturer:
            con["manufacturer"] = manufacturer

        invisible = con_dic.get("invisible")
        if not isinstance(invisible,bool):
            invisible = utils.str2bool(invisible) 
        if invisible is not None:
            con["invisible"] = invisible

        guest_id = con_dic.get("guest_id")
        if guest_id:
            con["guest_id"] = guest_id

        return con
        

    
