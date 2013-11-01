# -*- coding: utf-8 -*-

from datetime import date
from datetime import datetime
import decimal
import json

from flask import Response


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


def error(errcode, msg, **kwargs):
    result = {}
    result.update(kwargs)
    result["errcode"] = int(errcode)
    result["msg"] = msg
    return Response(jsondump(result), status=200, mimetype='application/json')


def success(msg='Request Succeed', **kwargs):
    result = {}
    result.update(kwargs)
    result["errcode"] = 0
    result["msg"] = msg
    return Response(jsondump(result), status=200, mimetype='application/json')
