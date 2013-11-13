# -*- coding: utf-8 -*-

import time

from o2olib import peewee
from o2olib.peewee import Q
import o2o_settings as settings


class SafeDatabase(peewee.PostgresqlDatabase):

    def get_conn(self):
        result = None
        while True:
            try:
                result = super(SafeDatabase, self).get_conn()
                cursor = result.cursor()
                cursor.execute("SELECT 1")
                break
            except Exception:
                try:
                    self.close()
                except:
                    time.sleep(1)
                continue
        return result


psql_db = SafeDatabase(
    host=settings.DBSETTINGS['HOST'],
    port=settings.DBSETTINGS['PORT'],
    user=settings.DBSETTINGS['USER'],
    password=settings.DBSETTINGS['PASSWD'],
    database=settings.DBSETTINGS['DBNAME']
    )


class ModelBase(peewee.Model):
    class Meta:
        database = psql_db
    @classmethod
    def build_con(cls,con_dic):
        print "con:%s" % con_dic
        con = None
        for k,v in con_dic.items():
            if v is not None:
                query = {}
                query[k] = v
                tmpCon = Q(**query)
                con = (con is not None) and con & tmpCon or tmpCon
        return con   

def update_model(model,dic):
    for key in dic.keys():
        v = dic[key]
        print "k:%s v:%s"% (key,v)
        if v is not None:
            model.__setattr__(key,v)
    return model
