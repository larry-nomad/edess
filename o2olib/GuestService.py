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
        raise QException(u"用户id不能为空")
    guests = gets({"id":id})
    if len(guests) == 0:
        rs = {}
    else:
        rs = guests[0]
    return rs

def add(guest):
    if not guest:
        raise QException(u"客户不能为空")
    check_email_existed(guest.get("email"))
    guest["id"] = None
    model = GuestModel().create()
    model = update_model(model,guest)
    model.save()
    return model.id


def update(guest):
    if not (guest and guest.get("id")):
        raise QException(u"客户id不能为空")
    id = guest.get("id")
    check_email_existed(guest.get("email"),id)
    model = GuestModel.get(id = id)
    if not guest.get("birthday"):
        guest["birthday"] = None
    update_model(model,guest)
    model.save()
    return model.id
    
def delete(id):
    if not id:
        raise QException(u"用户id不能为空")
    dq = DeleteQuery(GuestModel).where(id = id)
    return dq.execute()

def check_name_existed(name,id=None):
    guests = gets({"name":name})
    if len(guests) == 0:
        return
    else:
        guest = guests[0]
        if guest.get("id") == id:
            return 
    raise QException(u"用户名已存在")    

def check_email_existed(email,id=None):
    if not email:
        return
    guests = gets({"email":email})
    if len(guests) == 0:
        return
    else:
        guest = guests[0]
        if guest.get("id") == id:
            return 
    raise QException(u"邮件已存在")



