import aiohttp_jinja2

@aiohttp_jinja2.template('index.html.j2')
async def index(request):
    return {
        "relays": request.app["relays"],
        "dht11s": request.app["dht11s"],
        "dht22s": request.app["dht22s"],
        "cameras": request.app["cameras"]
    }