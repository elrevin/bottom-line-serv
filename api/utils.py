import json

from django.http import HttpResponse


def send_json(data):
    response = HttpResponse(json.dumps(data))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    return response
