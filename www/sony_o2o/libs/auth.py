# -*- coding: utf-8 -*-

import ldap
import md5
from flask import request, session
from opsapi_auth.libs.ajax import *
import settings
from opsapi_auth_lib import logger
from opsapi_auth_lib.utils import utils
from opsapi_auth_lib.models.__init__ import ClientModel
from flask import Response
from opsapi_auth.libs import ajax


def ldapLogin(user, passwd):
    l_user = "%s@qunarservers.com" % user
    scope = ldap.SCOPE_SUBTREE
    filter = "(sAMAccountName=%s)" % user
    retrieve_attributes = None

    try:
        con = ldap.open(settings.LDAP_HOST, settings.LDAP_PORT)
        con.simple_bind_s(l_user, passwd)
        #result_id = con.search(settings.LDAP_BASE, scope, filterstr=filter, attrlist=retrieve_attributes)
        #result_type, result_data = con.result(result_id, 1)
        return True
    except:
        return None

#    if len(result_data) < 1:
#        return None
#
#    result_data = result_data[0]
#    return result_data

def clientLogin(username, password):
    query = ClientModel.select().where(\
            ClientModel.username==username,\
            ClientModel.password==password)
    query_result = utils.getPwMap(query)
    if len(query_result) == 0:
        return False
    else:
        return True

# @decorator
class require_login(object):
    def __init__(self):
        pass

    def __call__(self, func):
        def invoke(*args, **kwargs):
            if request.authorization is not None:
                username = request.authorization['username']
                password = request.authorization['password']
                password = md5.new(password).hexdigest()
                check_client = clientLogin(username, password)
                if request.remote_addr not in settings.API_ALLOW_LIST:
                    logger.error('api ip %s is not in allow list.' % request.remote_addr)
                    return Response(ajax.ajax_error('require authorization'), status=401, mimetype='application/json')
                if check_client is True:
                    session['user_id'] = username
                    return func(*args, **kwargs)
                else:
                    return Response(ajax.ajax_error('require authorization'), status=401, mimetype='application/json')
            if not session.has_key("user_id"):
                return ajax_direct_login()
            return func(*args, **kwargs)

        invoke.__name__ = func.__name__
        return invoke

# @decorator
class require_post_field(object):
    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, func):
        def invoke(*args, **kwargs):
            if not request.form.has_key(self.field_name):
                return ajax_error(msg='not found key %s' % self.field_name)
            return func(*args, **kwargs)
        invoke.__name__ = func.__name__
        return invoke


