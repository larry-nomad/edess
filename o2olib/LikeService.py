# -*- coding: utf-8 -*-

from o2olib.utils import utils
from o2olib.models.like import LikeModel
from o2olib.peewee import  DeleteQuery,SelectQuery
from o2olib.models.modelbase import update_model
from datetime import datetime
from o2olib.QException import QException

def gets(con_dic):
    con = LikeModel.build_con(con_dic)
    if con:
        query = LikeModel.select().where(con)
    else:
        query = LikeModel.select()
    query_rs = utils.getPwMap(query)
    return query_rs

def get(con):
    likes = gets(con)
    if len(likes) == 0:
        like = {}
    else:
        like = likes[0]
    return like

def count_likes(con_dic):
    con = LikeModel.build_con(con_dic)
    sq = SelectQuery(LikeModel).where(con)
    return sq.count()
 
def add_or_update(like):
    like_id = update(like)
    if not like_id:
        like_id = add(like)
    return like_id
    
def add(like):
    if not like:
        raise QException(u"没有要插入数据")
    model = LikeModel().create()
    update_model(model,like)
    model.like_date = datetime.now()
    model.save()
    return model.id

def update(like):
    if not like:
        raise QException(u"没有要修改数据")
    dbLike = get(like)
    if dbLike:
        model = LikeModel().create()
        update_model(model,like)
        model.like_date = datetime.now()
        model.save()
        return model.id

def delete(like):
    if like:
        dbLike = get(like)
        if dbLike:
            delQuery = DeleteQuery(LikeModel).where(id = dbLike.get("id"))
            return delQuery.execute()


