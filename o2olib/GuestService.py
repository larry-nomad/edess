from o2olib.utils import utils
from o2olib import models
from o2olib.models.guest import GuestModel
from o2olib.peewee import Q


def get_guest(id):
    if id != '':
        query = GuestModel.select().where(Q(id=id))
        query_result = utils.getPwMap(query)
        if len(query_result) == 0:
            guest = {}
        else:
            guest = query_result[0]
        return guest


def add_guest(guest):
    if guest:
        guest_model = models.guest.GuestModel().create()
        guest_model.name = guest['name']
        guest_model.save()
        return guest_model.id


def update_guest(guest):
        guest_id = guest['id']
        query = GuestModel().select().where(Q(id=guest_id))
        guest_model = query.get()
        guest_model.save()
        return guest


def delete_guest(id):
    guest_id = id
    query = GuestModel().select().where(Q(id=guest_id))
    guest_model = query.get()
    guest_model.remove()
    return id
