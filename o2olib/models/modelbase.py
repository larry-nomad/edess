# -*- coding: utf-8 -*-

import time

from o2olib import peewee
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
            except Exception,ex:
                logger.exception(ex)
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
    def build_con(cls,con_dict):
        return cls.inner_build_con(con_dict)

    @classmethod
    def build_con_dict(cls,con_dict):
        return con_dict

    @classmethod
    def inner_build_con(cls,con_dic):
        logger.debug("ModelBase inner_build_con(cls:%s con_dic:%s)" % (cls,con_dic))
        con_dic = cls.build_con_dict(con_dic)
        con = None
        for k,v in con_dic.items():
            if v is not None and hasattr(cls,k):
                #query = {}
                #query[k] = v
                #tmpCon = Q(**query)
                #if hasattr(cls,k):
                val = v
                if isinstance(v,list):
                    val = v[0]
                logger.debug("ModelBase build_con(k:%s v:%s)"%(k,val))
                tmpCon = (getattr(cls,k)==v)
                con = (con is not None) and (con & tmpCon) or tmpCon
        return con   


def update_model(model,dic):
    logger.debug("update_model(model:%s dic:%s)"% (model,dic))
    for key in dic.keys():
        v = dic[key]
        if v is not None :#and hasattr(model,key):
            val = v
            if isinstance(v,list):
                val = v[0]
            logger.debug("update_model(k:%s v:%s)"%(key,val))
            if val:
                model.__setattr__(key,val)
    return model
