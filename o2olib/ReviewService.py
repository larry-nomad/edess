from o2olib.utils import utils
from o2olib.models.review import ReviewModel
from o2olib.peewee import Q
from datetime import datetime

def get_reviews(con_dic):
    con = _build_con(con_dic)
    if con:
        query = ReviewModel.select().where(con)
    else:
        query = ReviewModel.select()
    query_rs = utils.getPwMap(query)
    return query_rs

def add_review(review):
    if review:
        model = _build_review_model(review)
        model.review_date = datetime.now()
        model.save()
        return model.id

def update_review(review):
    if review:
        model = _build_review_model(review
                ,ReviewModel.get(id = review.get("id")))
        model.save()
        return model.id

def delete_review(id):
    if id:
        query = ReviewModel.delete().where(Q(id = id))
        query.execute()
        return id
        

def count_stars(con_dic):
    coursor =  ReviewModel.Meta.database.execute(
            """select ranked_stars,count(id) 
            from map_guest_reviews 
            where product_id = %s group by ranked_stars;"""
            ,(con_dic.get("product_id"),))
    items = coursor.fetchall()
    coursor.close()
    rs = []
    for item in items:
        rs.append({"ranked_stars": item[0],"count":item[1]})
    return rs

def _build_review_model(review, model = ReviewModel().create()):
     if review:
         product_id = review.get("product_id")
         guest_id = review.get("guest_id")
         is_approved = review.get("is_approved")
         comment = review.get("comment")
         ranked_stars = review.get("ranked_stars")
         if product_id:
             model.product_id = product_id
         if guest_id:
             model.guest_id = guest_id
         if is_approved is not None:
             model.is_approved = is_approved
         if comment:
             model.comment = comment
         if ranked_stars is not None:
             model.ranked_stars = ranked_stars
     print review
     return model
    

def _build_con(con_dic):
    id = con_dic.get("id")
    product_id = con_dic.get("product_id")
    guest_id = con_dic.get("guest_id")
    is_approved = con_dic.get("is_approved")
    con = None
    if id:
        con = Q(id = id)
    if product_id:
        pCon = Q(product_id = product_id)
        con = (con != None) and con & pCon or pCon
    if guest_id:
        gCon = Q(guest_id = guest_id)
        con = (con != None) and con & gCon or gCon
    if is_approved:
        aCon = Q(is_approved = is_approved)
        con = (con != None) and con & aCon or aCon
    return con
