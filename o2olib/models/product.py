# -*- coding: utf-8 -*-

from modelbase import ModelBase
from o2olib.peewee import IntegerField, CharField, BooleanField, TextField
from o2olib.utils import utils
from o2olib import logger


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
        logger.debug("ProductModel build_con(cls:%s con_dic:%s)" % (cls,con_dict))
        name = utils.get_val_from_dict(con_dict, "name")
        nCon = None
        if name:
            nCon = (ProductModel.name ** name)
            con_dict["name"] = None
        cCon = None
        category = utils.get_val_from_dict(con_dict, "category", "list")
        if category:
            cCon = (ProductModel.category << category)
            con_dict["category"] = None

        invisible = utils.get_val_from_dict(con_dict, "invisible")
#         invisible = None
#         if invisibles:
#             invisible = invisibles[0]
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
        

    
