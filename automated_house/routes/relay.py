from aiohttp import web
from traceback import format_exc
from .utils import pin_parse


async def switch_relay(request):
    """
    Incoming:
    {
        "pin": "switch-17,
        "isActive": 1
    }
    """
    response = web.Response()
    try:
        body = await request.json()
        _, pin = pin_parse(body["pin"])
        relay = request.app["relays"][pin]
        relay.on() if body["isActive"] else relay.off()
    except:
        print(format_exc())
        response = web.Response(status=400, reason=format_exc())
    return response

async def get_relay_status(request):
    """
    Incoming:
        ?pin=switch-17
    """
    try:
        _, pin = pin_parse(request.rel_url.query["pin"])
        relay = request.app["relays"][pin]
        response = web.json_response({"isActive": relay.is_active})
    except:
        print(format_exc())
        response = web.Response(status=400, reason=format_exc())
    return response
