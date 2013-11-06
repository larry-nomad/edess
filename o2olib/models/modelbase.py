# -*- coding: utf-8 -*-

import time

from o2olib import peewee
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
