# -*- encoding:utf-8 -*-

from flask import Flask
from flask.ext import restful
from sony_o2o.libs import session
from JsonEncoder import JsonEncoder
from flask.ext.restful.representations import json
from o2olib import logger
from JsonResult import JsonResult
import settings
import json as jjson
from o2olib.QException import QException
from o2olib.peewee import DoesNotExist
from settings import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.session_interface = session.SecureCookieSessionInterface()
_api = restful.Api()
_api.app = app
_api.endpoints = set()

json.settings.setdefault('cls', JsonEncoder)
json.settings.setdefault('separators', (',', ':'))

# logger setup
logger.log_dir = settings.LOG_PATH
logger.log_name = settings.LOG_WEB_NAME


@app.errorhandler(404)
def page_not_fount(error):
    logger.exception(error)
    msg = u"资源正在维护"
    return jjson.dumps(JsonResult().set_error_msg(msg).to_dic()), 404

@app.errorhandler(Exception)
def exception_handler(error):
    logger.exception(error)
    return jjson.dumps(JsonResult().set_error_msg(error.message).to_dic()),500 

@app.errorhandler(QException)
def special_exception_handler(error):
    logger.exception(error)
    return jjson.dumps(JsonResult().set_error_msg(error.message).to_dic()), error.code


@app.errorhandler(DoesNotExist)
def not_exist_exception_handler(error):
    logger.exception(error)
    msg = u"数据库中没有要更新的数据"
    return jjson.dumps(JsonResult().set_error_msg(msg).to_dic()), 404


@app.context_processor
def default_context_processor():
    result = {}
    result['title'] = settings.WEB_TITLE
    result['baseurl'] = settings.WEB_BASEURL
    return result

from sony_o2o.views.guest.Guest import Guest as v1_guest
_api.add_resource(v1_guest, '/v1/guest', '/v1/guest/<int:id>')

from sony_o2o.views.guest.Guest import Guests as v1_guest_list
_api.add_resource(v1_guest_list, '/v1/guests')

from sony_o2o.views.product.Product import Product as v1_product
_api.add_resource(v1_product, '/v1/product/<int:id>')

from sony_o2o.views.product.Product import Products as v1_products
_api.add_resource(v1_products, '/v1/products')

from sony_o2o.views.product.Product import Like as v1_like
_api.add_resource(v1_like, '/v1/like', '/v1/like/<int:id>')

from sony_o2o.views.product.Product import Likes as v1_likes
_api.add_resource(v1_likes, '/v1/likes')

from sony_o2o.views.product.Product import Review as v1_review
_api.add_resource(v1_review, '/v1/review', '/v1/review/<int:id>')

from sony_o2o.views.product.Product import Reviews as v1_reviews
_api.add_resource(v1_reviews, '/v1/reviews')

from sony_o2o.views.product.Product import ReviewsForGuest as v1_my_reviews
_api.add_resource(v1_my_reviews, '/v1/my/reviews')

from sony_o2o.views.product.Product import Manual as v1_manual
_api.add_resource(v1_manual, '/v1/manual', '/v1/manual/<int:id>')

from sony_o2o.views.product.Product import Manuals as v1_manuals
_api.add_resource(v1_manuals, '/v1/manuals')

from sony_o2o.views import hot
app.register_blueprint(hot.BP, url_prefix='/')

from sony_o2o.views import search
app.register_blueprint(search.BP, url_prefix='/')

from sony_o2o.views import detail
app.register_blueprint(detail.BP, url_prefix='/')

from sony_o2o.views import store
app.register_blueprint(store.BP, url_prefix='/')

from sony_o2o.views import login
app.register_blueprint(login.BP, url_prefix='/')
