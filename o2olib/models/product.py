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
    def build_con(cls,con_dict):
        name = con_dict.get("name")
        nCon = None
        if name:
            print("name: %s"%name)
            nCon = (ProductModel.name ** name)
            con_dict["name"] = None

        invisible = con_dict.get("invisible")
        if not isinstance(invisible,bool):
            invisible = utils.str2bool(invisible) 
        if invisible is not None:
            con_dict["invisible"] = invisible
        
        con = ModelBase.build_con(con_dict)

        if nCon:
            con = (con is not None) and (con & nCon) or nCon
        
        return con
        

    
