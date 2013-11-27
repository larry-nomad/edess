# -*- coding: utf-8 -*-

from o2olib.utils import utils
from o2olib.models.review import ReviewModel
from o2olib.models.review import GuestModel
from datetime import datetime
from o2olib.models.modelbase import update_model
from o2olib.QException import QException
from o2olib.peewee import desc

def gets(con_dic):
    con = ReviewModel.build_con(con_dic)
    if con:
        query = ReviewModel.select().where(con)
    else:
        query = ReviewModel.select()
    query_rs = utils.getPwMap(query)
    return query_rs

def get_reviews_for_guest(con_dic):
    if not(con_dic and con_dic.get("guest_id")):
        raise QException(u"用户id不能为空")
    con = ReviewModel.build_con(con_dic)
    query = ReviewModel.select().join(GuestModel).where(con).order_by(desc("review_date"))
    query_rs = utils.getPwMap(query)
    return query_rs

def add(review):
    if not(review and review.get("comment")):
        raise QException(u"说点什么吧")
    model = ReviewModel.create()
    update_model(model,review)
    model.review_date = datetime.now()
    model.save()
    return model.id

def update(review):
    if not(review and review.get("comment")):
        raise QException(u"说点什么吧")
    model = ReviewModel.get(
                id = review.get("id")
                ,guest_id = review.get("guest_id"))
    update_model(model,review)
    model.save()
    return model.id

def delete(review):
    if not (review and review.get("id")):
        raise QException(u"评论id不能为空")
    if not review.get("guest_id"):
        raise QException(u"用户id不能为空")
    query = ReviewModel.delete().where(id = review.get("id"),guest_id = review.get("guest_id"))
    return query.execute()
        

def count_stars(con_dic):
    coursor =  ReviewModel.Meta.database.execute(
            """select ranked_stars,count(id) 
            from map_guest_reviews 
            where product_id = %s group by ranked_stars;"""
            ,(con_dic.get("product_id"),))
    items = coursor.fetchall()
    coursor.close()
    rs = {}
    for item in items:
        k = item[0]
        if k:
            rs[k] = item[1]
        #rs.append({"ranked_stars": item[0],"count":item[1]})
    return rs


