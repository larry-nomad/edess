# -*- encoding:utf-8 -*-

from flask import Flask
from flask.ext import restful
from sony_o2o.libs import session
from o2olib import logger
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

'''
_api.add_resource(v1_guest, '/v1/guest')
'''
_api.add_resource(v1_guest, '/v1/guest/<int:id>')

from sony_o2o.views.product.Product import Product as v1_product

_api.add_resource(v1_product, '/v1/product/<int:id>')

from sony_o2o.views.product.Product import ProductList as v1_products

_api.add_resource(v1_products, '/v1/products', '/v1/products/<string:name>/<string:category>')

from sony_o2o.views.product.Like import Like as v1_like

_api.add_resource(v1_like, '/v1/like', '/v1/like/<int:id>', '/v1/like/product/<int:product_id>')

from sony_o2o.views.guest.Guest import GuestList as v1_guest_list

_api.add_resource(v1_guest_list, '/v1/guest/list')


from sony_o2o.views import index
app.register_blueprint(index.BP, url_prefix='/')
