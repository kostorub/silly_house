from aiohttp import web
from traceback import format_exc
from .utils import id_from_str


async def get_dht11_status(request):
    """
    Incoming:
        ?pin=dht11-17
    """
    try:
        pin = id_from_str(request.rel_url.query["pin"])
        dht11 = request.app["dht11s"][pin]
        t, h = dht11.status()
        response = web.json_response({"temperature": t, "humidity": h})
    except:
        print(format_exc())
        response = web.Response(status=400, reason=format_exc())
    return response