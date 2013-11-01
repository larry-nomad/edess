# -*- coding: utf-8 -*-

import time

from opsapi_auth_lib import peewee
import opsapi_auth_settings as settings


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
    host=settings.PGSQL_HOST,
    port=settings.PGSQL_PORT,
    user=settings.PGSQL_USER,
    password=settings.PGSQL_PASSWD,
    database=settings.PGSQL_DBNAME
    )


class ModelBase(peewee.Model):
    class Meta:
        database = psql_db
