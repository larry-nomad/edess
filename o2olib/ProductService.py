# -*- coding: utf-8 -*-

from o2olib.utils import utils
from o2olib.models.product import ProductModel
from o2olib.models.like import LikeModel
from o2olib.models.manual import ManualModel
from QException import QException
from o2olib.peewee import Q

def get(id):
    if not id:
        raise QException(u"产品id不能为空")
    query_rs = gets({"id": id})
    if len(query_rs) == 0:
        product = {}
    else:
        product = query_rs[0]
    return product

def gets(con_dic):
    con = ProductModel.build_con(con_dic)
    if con:
        query = ProductModel.select().where(con)
    else:
        query = ProductModel.select()
    query_rs = utils.getPwMap(query)
    return query_rs

def get_products_for_like(con_dic):
    if not(con_dic and con_dic.get("guest_id")):
        raise QException(u"客户id不能为空")
    
    con = ProductModel.build_con(con_dic)
   
   # print "test:%s %s"%(ProductModel.get("invisible"),ProductModel.invisible == True)
    query = ProductModel.select().join(
             LikeModel).where(con)
    query_rs = utils.getPwMap(query)
    return query_rs

def get_products_for_manual(con_dic):
    if not(con_dic and con_dic.get("guest_id")):
        raise QException(u"客户id不能为空")
    
    con = ProductModel.build_con(con_dic)
    query = ProductModel.select().join(
             ManualModel).where(con)
    query_rs = utils.getPwMap(query)
    return query_rs

    


