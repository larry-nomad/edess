#!/usr/bin/env python
#coding=utf-8
'base setting'

import os

# 获取app路径
# 1、从OPSDB_PATH环境变量中取
# 2、默认值


def _get_application_path():
    'get path'
    app_path = None
    default = '/usr/share/sony_o2o'
    env_path = os.environ.get("GPM_PATH", "")
    if env_path == "":
        app_path = default
    else:
        app_path = env_path
    return app_path

# calc app_path
APP_PATH = _get_application_path()

# log
LOG_PATH = os.path.join(APP_PATH, 'logs')
LOG_DAEMON_NAME = 'daemon'
LOG_WEB_NAME = 'web'

# pgsql
DBSETTINGS = {
    'HOST': '127.0.0.1',
    'PORT': 5432,
    'USER': 'postgres',
    'PASSWD': 'keyqunars1234',
    'DBNAME': 'sony_o2o',
    }

# web
FCGI_HOST = '127.0.0.1'
FCGI_PORT = 9010
FCGI_PID = '/tmp/web.run'

WEB_LOGIN_NORMAL_INTERVAL = 60 * 30
WEB_LOGIN_SAVED_INTERVAL = 60 * 60 * 24 * 7
WEB_PID_FILE = '/tmp/sony_o2o.pid'
WEB_TITLE = u'SONY O2O API'
WEB_BASEURL = ''
