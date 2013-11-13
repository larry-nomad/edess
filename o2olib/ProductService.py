from o2olib.utils import utils
from o2olib.models.product import ProductModel
from o2olib.models.like import LikeModel
from o2olib.models.manual import ManualModel

def get_product(id):
    query_rs = get_products({"id": id})
    if len(query_rs) == 0:
        product = {}
    else:
        product = query_rs[0]
    return product

def get_products(con_dic):
    con = ProductModel.build_con(con_dic)
    if con:
        query = ProductModel.select().where(con)
    else:
        query = ProductModel.select()
    query_rs = utils.getPwMap(query)
    return query_rs

def get_products_for_like(con_dic):
    con = ProductModel.build_con(con_dic)
    if con:
        query = ProductModel.select().join(
             LikeModel).where(con)
        query_rs = utils.getPwMap(query)
        return query_rs
    else:
        raise Exception("guest_id is None")

def get_products_for_manual(con_dic):
    con = ProductModel.build_con(con_dic)
    if con:
        query = ProductModel.select().join(
             ManualModel).where(con)
        query_rs = utils.getPwMap(query)
        return query_rs
    else:
        raise Exception("guest_id is None")


    


