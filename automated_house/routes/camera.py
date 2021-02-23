from aiohttp import web
from traceback import format_exc
from .utils import id_from_str


async def get_current_frame(request):
    """
    Incoming:
        ?id=camera-1
    """
    try:
        id = id_from_str(request.rel_url.query["id"])
        camera = request.app["cameras"][id]
        response = web.Response(body=camera.current_frame, headers={"Content-Type": "image/jpeg"})
    except:
        print(format_exc())
        response = web.Response(status=400, reason=format_exc())
    return response