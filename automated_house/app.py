import os
import struct
import asyncio
from functools import partial
import multiprocessing as mp

import aiohttp_jinja2
import jinja2
from aiohttp import web

from models.button import Button
from models.device_list import DeviceList
from speech_recognition import SpeechRecognition
from models.dht11 import DHT11
from models.dht22 import DHT22
from models.relay import Relay
from models.relay433 import Relay433
from config import config
from routes.index import index 
from routes.relay import switch_relay, get_relay_status 
from routes.dht import get_dht_status
from routes.camera import get_current_frame
from camera import video_capture
from models.camera import Camera


dirname, _ = os.path.split(os.path.abspath(__file__))
static_path = os.path.join(dirname, "www")

relays = DeviceList([
    Relay(
        relay["bcm_pin"],
        relay["phrase_on"],
        relay["phrase_off"],
        relay["name"]) for relay in config.get("relays", [])])
relays433 = [
    Relay433(
        relay["code_on"],
        relay["code_off"],
        relay["name"],
        relay["phrase_on"],
        relay["phrase_off"]) for relay in config.get("relays433", [])]
relays.extend(relays433)

buttons = DeviceList([
    Button(
        button["bcm_pin"],
        button["control_pin"],
        button["name"],
        relays) for button in config.get("buttons", [])])

dht11s = DeviceList([
    DHT11(
        dht11["bcm_pin"],
        dht11["name"],
        dht11["phrase"]) for dht11 in config.get("dht11s", [])])

dht22s = DeviceList([
    DHT22(
        dht22["bcm_pin"],
        dht22["name"],
        dht22["phrase"]) for dht22 in config.get("dht22s", [])])

manager = mp.Manager()

cameras = DeviceList()
for camera in config.get("cameras", []):
    c = manager.Namespace()
    c.id = camera["id"]
    c.name = camera["name"]
    c.url = camera["url"]
    c.current_frame = None
    cameras.append(c)
    p = mp.Process(target=video_capture, args=(c,))
    p.start()

loop = asyncio.get_event_loop()

# model_path = os.environ.get("MODEL_PATH", "automated_house/model")
# sr = SpeechRecognition(model_path, config, relays, loop)


# for camera in cameras:
#     loop.create_task(video_capture(camera))

app = web.Application()
app["relays"] = relays
app["dht11s"] = dht11s
app["dht22s"] = dht22s
app["cameras"] = cameras
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(static_path))
app.add_routes([web.get('/', index)])
app.add_routes([web.post('/relay', switch_relay)])
app.add_routes([web.get('/relay', get_relay_status)])
app.add_routes([web.get('/dht', get_dht_status)])
app.add_routes([web.get('/camera/current_frame', get_current_frame)])
app.add_routes([web.static('/', static_path)])
web.run_app(app, host=config["server"]["host"], port=config["server"]["port"])
