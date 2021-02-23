import os
import struct
import asyncio
from functools import partial

import aiohttp_jinja2
import jinja2
from aiohttp import web

from models.button import Button
from models.device_list import DeviceList
# from src.speech_recognition import SpeechRecognition
from models.dht11 import DHT11
from models.relay import Relay
from config import config
from routes.index import index 
from routes.relay import switch_relay, get_relay_status 
from routes.dht11 import get_dht11_status
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
        relay["name"]) for relay in config["relays"]])

buttons = DeviceList([
    Button(
        button["bcm_pin"],
        button["control_pin"],
        button["name"],
        relays) for button in config["buttons"]])

dht11s = DeviceList([
    DHT11(
        dht11["bcm_pin"],
        dht11["name"],
        dht11["phrase"]) for dht11 in config["dht11s"]])

cameras = DeviceList([
    Camera(
        camera["id"],
        camera["name"],
        camera["url"]) for camera in config["cameras"]])


loop = asyncio.get_event_loop()

# model_path = os.environ.get("MODEL_PATH", "home_service/model")
# sr = SpeechRecognition(model_path, config, relays, loop)

for camera in cameras:
    loop.create_task(video_capture(camera))

app = web.Application()
app["relays"] = relays
app["dht11s"] = dht11s
app["cameras"] = cameras
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(static_path))
app.add_routes([web.get('/', index)])
app.add_routes([web.post('/relay', switch_relay)])
app.add_routes([web.get('/relay', get_relay_status)])
app.add_routes([web.get('/dht11', get_dht11_status)])
app.add_routes([web.get('/camera/current_frame', get_current_frame)])
app.add_routes([web.static('/', static_path)])
web.run_app(app, host=config["server"]["host"], port=config["server"]["port"])
