# -*- coding: utf-8 -*-

from o2olib.utils import utils
from o2olib.models.productimg import ProductImgModel

def gets(con_dic):
    con = ProductImgModel.build_con(con_dic)
    if con:
        query = ProductImgModel.select().where(con)
    else:
        query = ProductImgModel.select()
    query_rs = utils.getPwMap(query)
    from o2olib import logger
    logger.info(query_rs)
    return query_rs

