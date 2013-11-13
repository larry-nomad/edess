# -*- encoding:utf-8 -*-

from flask import Flask
from flask.ext import restful
from sony_o2o.libs import session
from sony_o2o.JsonEncoder import JsonEncoder
from flask.ext.restful.representations import json
from o2olib import logger
import settings


app = Flask(__name__)
app.session_interface = session.SecureCookieSessionInterface()
_api = restful.Api(app)
#app.json_encoder = je
json.settings.setdefault('cls',JsonEncoder)
json.settings.setdefault('separators',(',',':::::'))

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
_api.add_resource(v1_guest, '/v1/guest', '/v1/guest/<int:id>')

from sony_o2o.views.guest.Guest import GuestList as v1_guest_list
_api.add_resource(v1_guest_list, '/v1/guests')
_api.add_resource(v1_guest_list, '/v1/guest/list')

from sony_o2o.views.product.Product import Product as v1_product
_api.add_resource(v1_product, '/v1/product/<int:id>')

from sony_o2o.views.product.Product import ProductList as v1_products
_api.add_resource(v1_products, '/v1/products')

from sony_o2o.views.product.Product import Like as v1_like
_api.add_resource(v1_like, '/v1/like', '/v1/like/<int:id>')

from sony_o2o.views.product.Product import Review as v1_review
_api.add_resource(v1_review, '/v1/review', '/v1/review/<int:id>')

from sony_o2o.views.product.Product import Reviews as v1_reviews
_api.add_resource(v1_reviews,'/v1/reviews')

from sony_o2o.views.product.Product import Manual as v1_manual
_api.add_resource(v1_manual, '/v1/manual', '/v1/manual/<int:id>')

from sony_o2o.views.product.Product import Manuals as v1_manuals
_api.add_resource(v1_manuals, '/v1/manuals')

from sony_o2o.views import index
app.register_blueprint(index.BP, url_prefix='/')
