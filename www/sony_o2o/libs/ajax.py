# -*- coding: utf-8 -*-

import json
import datetime
import decimal
from datetime import datetime, date


def _jsonfy(mix):
    result = None
    if isinstance(mix, list):
        result = []
        for i in mix:
            result.append(_jsonfy(i))
    elif isinstance(mix, dict):
        result = {}
        for k, v in mix.items():
            k = _jsonfy(k)
            v = _jsonfy(v)
            result[k] = v
    elif isinstance(mix, datetime):
        result = mix.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(mix, date):
        result = mix.strftime('%Y-%m-%d')
    elif isinstance(mix, decimal.Decimal):
        result = float(mix)
    else:
        return mix
    return result


def jsondump(mix):
    mix = _jsonfy(mix)
    return json.dumps(mix)


def ajax_error(msg, **kwargs):
    result = {}
    result.update(kwargs)
    result["success"] = False
    result["msg"] = msg
    return jsondump(result)


def ajax_success(msg, **kwargs):
    result = {}
    result.update(kwargs)
    result["success"] = True
    result["msg"] = msg
    return jsondump(result)

def ajax_template_tree(**kwargs):
    result = {}
    result.update(kwargs)
    result["text"] = "."
    return jsondump(result)

def ajax_direct_login():
    result = {}
    result["success"] = "expire"
    result["redirect"] = "/auth/login"
    return jsondump(result)


def ajax_return(data):
    return jsondump(data)



