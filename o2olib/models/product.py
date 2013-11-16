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
        print con_dict
        name = con_dict.get("name")
        nCon = None
        if name:
            nCon = (ProductModel.name ** name[0])
            con_dict["name"] = None
        cCon = None
        category = con_dict.get("category")
        if category:
            cCon = (ProductModel.category << category)
            con_dict["category"] = None

        invisibles = con_dict.get("invisible")
        invisible = None
        if invisibles:
            invisible = invisibles[0]
        if not isinstance(invisible,bool):
            invisible = utils.str2bool(invisible) 
        if invisible is not None:
            con_dict["invisible"] = invisible
        
        con = cls.inner_build_con(con_dict)

        if nCon:
            con = (con is not None) and (con & nCon) or nCon
        if cCon:
            con = (con is not None) and (con & cCon) or cCon

        return con
        

    
