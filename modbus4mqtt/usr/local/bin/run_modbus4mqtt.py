from modbus4mqtt import modbus4mqtt
from typing import Callable, cast
import yaml
import logging

config_file_path = "/etc/modbus4mqtt/config.yml"

def init_log():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )

with open(config_file_path,'r') as f:
    init_log()
    config_file = yaml.safe_load(f)

    logging.info("loaded config.yaml",config_file)

    orig_main = cast(
        Callable,
        modbus4mqtt.main.callback
    )

    orig_main(
        **config_file['mqtt'],
        **config_file['security'],
        config=config_file['config']
    )

