import numpy as np
import cv2
import time
import json
from typing import Dict
import base64
import asyncio

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
        print(f"execution time: {result*1000}ms.")
        return restult
    return inner

def deserialize(img_base64) -> np.ndarray:
    
    img_bytes = base64.b64decode(img_base64)  # Decode base64 string to bytes
    img_np = np.frombuffer(img_bytes, dtype=np.uint8) # Convert bytes to NumPy array
    img_restored = cv2.imdecode(img_np, cv2.IMREAD_COLOR) # Decode image
    return img_restored


def serialize(img: np.ndarray) -> str:
    
    _, buffer = cv2.imencode('.png', img) # Encode image to PNG (or JPEG) bytes    
    img_base64 = base64.b64encode(buffer).decode('utf-8') # Convert bytes to base64 string
    return img_base64