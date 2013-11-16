# -*- coding: utf-8 -*-

from modelbase import ModelBase
from o2olib.peewee import *


class GuestModel(ModelBase):
    class Meta:
        db_table = 'table_guest'
    id = IntegerField()
    name = CharField()
    gender = CharField()
    email = CharField()
    birthday = DateTimeField(default=None)
    telephone = CharField()
    register_date = DateTimeField(default=None)
    last_active_date = DateTimeField(default=None)
    qq = CharField()
    qq_openid = CharField()
    wechat = CharField()
    twitter = CharField()
    weibo = CharField()
    facebook = CharField()
    google_plus = CharField()
    alipay = CharField()
    credit_points = IntegerField()
    influence_point = IntegerField()
    status = CharField()


