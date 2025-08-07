import time
import json
from typing import Dict


def load_json(config_addr: str="/home/app/alignment/config/config.json") -> Dict[str, any]:
    try:
        with open(config_addr, 'r') as f:
            data = json.load(f)
            return data
    except Exception as error:
        print(f"Cant load json config file. '{error}'")


def caculate_execution_time(func):
    def inner(*args):
        stime = time.time()
        restult = func(*args)
        etime = time.time()
        result = etime - stime
        print(f"execution time: {result}s.")
        return restult
    return inner

