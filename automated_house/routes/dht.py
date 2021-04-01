from aiohttp import web
from traceback import format_exc
from .utils import pin_parse


async def get_dht_status(request):
    """
    Incoming:
        ?pin=dht11-17
    """
    try:
        dht_type, pin = pin_parse(request.rel_url.query["pin"])
        dht = request.app[dht_type + "s"][pin]
        t, h = dht.status()
        response = web.json_response({"temperature": t, "humidity": h})
    except:
        print(format_exc())
        response = web.Response(status=400, reason=format_exc())
    return response