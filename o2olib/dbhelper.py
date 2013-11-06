# -*- coding: utf-8 -*-

from opsapi_auth_lib.peewee import Q


def GenerateWhere(key, op, value):
    if op == 'eq':
        return Q(**{"%s" % key: value})
    elif op == 'neq':
        return Q(**{"%s__ne" % key: value})
    elif op == 'like':
        return Q(**{"%s__icontains" % key: value})
