# -*- coding: utf-8 -*-

from o2olib.utils import utils
from o2olib.models.store import StoreModel


def gets(con_dic):
    con = StoreModel.build_con(con_dic)
    if con:
        query = StoreModel.select().where(con)
    else:
        query = StoreModel.select()
    query_rs = utils.getPwMap(query)
    return query_rs



