import os
from models.configuration import Configuration


config_path = os.environ.get("CONFIG_PATH")
config = Configuration(config_path, "configuration.yaml")