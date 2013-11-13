from o2olib.utils import utils
from o2olib.models.guest import GuestModel
from o2olib.models.modelbase import update_model
from o2olib.peewee import Q

def get_guests(con_dic):
    con = _build_con(con_dic)
    if con:
        query = GuestModel.select().where(con)
    else:
        query = GuestModel.select()
    return utils.getPwMap(query)

def add_guest(guest):
    if guest:
        model = GuestModel().create()
        model = update_model(model,guest)
        model.save()
        return model.id


def update_guest(guest):
    if guest:
        model = GuestModel.get(id = guest.get("id"))
        update_model(model,guest)
        model.save()
        return model.id
    
def delete_guest(id):
    guest_id = id
    query = GuestModel().select().where(Q(id=guest_id))
    guest_model = query.get()
    guest_model.delete()
    return id

def _build_con(con_dic):
    con = None
    for k,v in con_dic.items():
        if v is not None:
            query = {}
            query[k] = v
            tmpCon = Q(**query)
            con = (con is not None) and con & tmpCon or tmpCon
    return con   
