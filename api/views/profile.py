import re
from django.http import HttpResponse
from django.http import HttpRequest
from django.utils.crypto import get_random_string

from api.utils import send_json
from po.models import Device


def get_profile_data_view(request: HttpRequest, uuid: str, token: str):
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
    """
        :type: Device
    """

    if not device:
        return send_json({
            'status': 'error',
            'code': 'DEVICE_NOT_FOUND',
        })

    devices = Device.objects.filter(member_id=device.member_id).all()

    qrCode = get_random_string(3)+str(device.member_id)+"|"+get_random_string(64)

    list = []

    for d in devices:
        list.append({
            "uuid": d.uuid,
            "token": d.token,
            "model": d.model,
        })

    ret = {
        'qrCode': qrCode,
        'devices': list,
    }

    return send_json({
        'status': 'ok',
        'data': ret,
    })
