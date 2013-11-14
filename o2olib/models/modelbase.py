# -*- coding: utf-8 -*-

import time

from o2olib import peewee
from o2olib.peewee import Q
import o2o_settings as settings
import o2olib.logger as logger


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
        logger.info("ModelBase build_con(cls:%s con_dic:%s)" % (cls,con_dic))
        con_dic = cls.build_con_dict(con_dic)
        con = None
        for k,v in con_dic.items():
            if v is not None:
                #query = {}
                #query[k] = v
                
                #tmpCon = Q(**query)
                tmpCon = (getattr(cls,k) == v)
                print tmpCon
                con = (con is not None) and (con & tmpCon) or tmpCon
        return con   

    @classmethod
    def build_con_dict(cls,con_dic):
        return con_dic

def update_model(model,dic):
    logger.info("update_model(model:%s dic:%s)"% (model,dic))
    for key in dic.keys():
        v = dic[key]
        if v is not None:
            model.__setattr__(key,v)
    return model
