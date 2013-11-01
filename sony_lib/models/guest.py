# -*- coding: utf-8 -*-

from modelbase import ModelBase
from opsapi_auth_lib.peewee import *


class AuthUserModel(ModelBase):
    class Meta:
        db_table = 'tb_auth_user'
    id = IntegerField()
    username = CharField()
    base_group_id = CharField()
    extended_permission_id_list = CharField()


class AuthGroupModel(ModelBase):
    class Meta:
        db_table = 'map_auth_group'
    id = IntegerField()
    group = CharField()
    role_id_list = CharField()


class AuthRoleModel(ModelBase):
    class Meta:
        db_table = 'map_auth_role'
    id = IntegerField()
    role = CharField()
    description = CharField()


class AuthTokenModle(ModelBase):
    class Meta:
        db_table = 'tb_auth_token'
    id = IntegerField()
    token = CharField()
    permission_id_list = CharField()
