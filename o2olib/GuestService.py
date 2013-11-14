# -*- coding: utf-8 -*-

from o2olib.utils import utils
from o2olib.models.guest import GuestModel
from o2olib.models.modelbase import update_model
from o2olib.QException import QException 
from o2olib.peewee import DeleteQuery

def gets(con_dic):
    con = GuestModel.build_con(con_dic)
    if con:
        query = GuestModel.select().where(con)
    else:
        query = GuestModel.select()
    return utils.getPwMap(query)

def get(id):
    if not id:
        raise QException(u"客户id不能为空")
    guests = gets({"id":id})
    if len(guests) == 0:
        rs = {}
    else:
        rs = guests[0]
    return rs

def add(guest):
    if not guest:
        raise QException(u"客户不能为空")
    guest["id"] = None
    model = GuestModel().create()
    model = update_model(model,guest)
    model.save()
    return model.id


def update(guest):
    if not (guest and guest.get("id")):
        raise QException(u"客户id不能为空")
    id = guest.get("id")
    model = GuestModel.get(id = id)
    update_model(model,guest)
    model.save()
    return model.id
    
def delete(id):
    if not id:
        raise QException(u"客户id不能为空")
    dq = DeleteQuery(GuestModel).where(id = id)
    return dq.execute()


