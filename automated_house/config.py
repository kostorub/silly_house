import os
from models.configuration import Configuration


config_path = os.environ.get("CONFIG_PATH")
if config_path:
    config = Configuration(config_path, "configuration.yaml")
else:
    raise Exception("Set CONFIG_PATH env variable which contains configuration.yaml on this path")