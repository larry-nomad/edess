from o2olib.utils import utils
from o2olib import models
from o2olib.models.product import ProductModel
from o2olib.peewee import Q

def get_product(id):
    if id != '':
        queryRs = get_products({"id": id})
        if len(queryRs) == 0:
            product = {}
        else:
            product = queryRs[0]
        return product

def get_products(conDic):
    con = build_con(conDic)
    if con:
        query = ProductModel.select().where(build_con(conDic))
    else:
        query = ProductModel.select().where()
    query_result = utils.getPwMap(query)
    return query_result

def build_con(conDic):
    id = conDic.get("id")
    name = conDic.get("name")
    category = conDic.get("category")
    manufacturer = conDic.get("manufacturer")
    invisible = conDic.get("invisible")
    con = None
    if id:
        con = Q(id = id)
    if name:
        nameCon = Q(name = name)
        con = (con != None) and con & nameCon or nameCon
    if category:
        cCon  = Q(category = category)
        con = (con != None) and con & cCon or cCon
    if manufacturer:
        mCon = Q(manufacturer = manufacturer)
        con = (con !=None) and con & mCon or mCon
    if invisible != None:
        iCon = Q(invisible = invisible)
        con = (con != None) and con & iCon or iCon
    return con

