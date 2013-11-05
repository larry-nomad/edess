# -*- coding: utf-8 -*-

from modelbase import ModelBase
from opsapi_auth_lib.peewee import *


class GuestModel(ModelBase):
    class Meta:
        db_table = 'table_guest'
    id = IntegerField()
    name = CharField()
    gender = CharField()
    telephone = CharField()
    extended_permission_id_list = CharField()
