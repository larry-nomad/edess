from o2olib.utils import utils
from o2olib import models
from o2olib.models.like import LikeModel
from o2olib.peewee import Q, DeleteQuery, SelectQuery

def get_likes(con):
    if con:
        likeId = con.get("id")
        productId = con.get("productId")
        guestId = con.get("guestId")
        if likeId:
            con = Q(id = likeId)
        elif productId and guestId:
            con = Q(product_id = productId, guest_id = guestId)
        elif productId:
            con = Q(product_id = productId)
        elif guestId:
            con = Q(guest_id = guestId)
        else:
            con = Q()
        query = LikeModel.select().where(con)
        queryRs = utils.getPwMap(query)
        return queryRs

def get_like(con):
    if not(con.get("id") or (con.get("productId") and con.get("guestId"))):
        return {};
    likes = get_likes(con)
    if len(likes) == 0:
        like = {}
    else:
        like = likes[0]
    return like

def count_likes(conDic):
    con = build_con(conDic)
    sq = SelectQuery(LikeModel).where(con)
    return sq.count()

    
def build_con(conDic):
    if conDic:
        likeId = conDic.get("id")
        productId = conDic.get("productId")
        guestId = conDic.get("guestId")
        if likeId:
            con = Q(id = likeId)
        elif productId and guestId:
            con = Q(product_id = productId, guest_id = guestId)
        elif productId:
            con = Q(product_id = productId)
        elif guestId:
            con = Q(guest_id = guestId)
        else:
            con = Q()
        return con

def add_like(like):
    if like:
        dbLike = get_like(like)
        if not dbLike:
            model = models.like.LikeModel().create()
            model.product_id = like.get('productId')
            model.guest_id = like.get('guestId')
            model.save()
            return model.id
        else:
            return dbLike.get("id")

def delete_like(like):
    if like:
        dbLike = get_like(like)
        if dbLike:
            delQuery = DeleteQuery(LikeModel).where(id = dbLike.get("id"))
            delQuery.execute()
            return dbLike.get("id")
