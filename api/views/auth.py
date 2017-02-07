import re
from urllib.parse import unquote

from django.http import HttpResponse
from django.http import HttpRequest
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt

from api.utils import send_json
from po.models import Device
from po.models import Member


def device_auth_view(request: HttpRequest, token, uuid):
    p = re.compile("^[a-zA-Z0-9]+$")
    if not token or not p.match(token):
        return send_json({
            'status': 'error',
            'code': 'TOKEN_IS_EMPTY',
        })

    if not uuid or not p.match(uuid):
        return send_json({
            'status': 'error',
            'code': 'UUID_IS_EMPTY',
        })

    device = Device.objects.filter(token=token, uuid=uuid).first()

    if not device:
        return send_json({
            'status': 'error',
            'code': 'DEVICE_NOT_FOUND',
        })

    return send_json({
        'status': 'ok',
    })


def member_auth_view(request: HttpRequest, uuid, model):
    if model:
        model = unquote(model).replace("+", " ")
    else:
        model = "Unknown model"
    p = re.compile("^[a-zA-Z0-9]+$")
    if not uuid or not p.match(uuid):
        return send_json({
            'status': 'error',
            'code': 'UUID_IS_EMPTY',
        })

    device = Device.objects.filter(uuid=uuid).first()
    """
        :type: Device
    """

    if device:
        token = device.token
        return send_json({
            'status': 'ok',
            'token': token,
        })

    member = Member()
    member.save()

    token = get_random_string(64)

    device = Device()
    device.token = token
    device.uuid = uuid
    device.model = model
    device.member = member
    device.save()

    return send_json({
        'status': 'ok',
        'token': token,
    })
