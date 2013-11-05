# -*- encoding:utf-8 -*-

from flask import Flask
from flask.ext import restful

from sony_lib import logger
from sony_o2o.libs import session
import settings


app = Flask(__name__)
app.session_interface = session.SecureCookieSessionInterface()
_api = restful.Api(app)

# logger setup
logger.log_dir = settings.LOG_PATH
logger.log_name = settings.LOG_WEB_NAME


@app.context_processor
def default_context_processor():
    result = {}
    result['title'] = settings.WEB_TITLE
    result['baseurl'] = settings.WEB_BASEURL
    return result

from sony_o2o.views.guest.Guest import Guest as v1_guest

_api.add_resource(v1_guest, '/v1/guest/<int:id>')
