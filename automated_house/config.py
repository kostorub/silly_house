import os
from models.configuration import Configuration


config_path = os.environ.get("SERVER_CONFIG_PATH", "automated_house")
config = Configuration(config_path, "configuration.yaml")