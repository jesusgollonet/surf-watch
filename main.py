import streamlink
import cv2 as cv
import time
from datetime import datetime
import json
from modules import sw_util, capture_frame


def load_config(config_file):
    with open(config_file) as f:
        return json.load(f)


webcams = load_config(".config.json").get("webcams")

for webcam in webcams:
    print(webcam.get("url"))
    if ".m3u8" in webcam.get("url"):
        webcam["m3u8_url"] = webcam.get("url")
    else:
        webcam["m3u8_url"] = sw_util.get_sw_stream_url_for_page(webcam.get("url"))

while True:
    for webcam in webcams:
        print(webcam.get("m3u8_url"))
        capture_frame.capture_frame(webcam.get("m3u8_url"), webcam.get("name"))
    time.sleep(5)
