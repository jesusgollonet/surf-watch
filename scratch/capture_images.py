import streamlink
import cv2 as cv
import time
from datetime import datetime
import json


def load_config(config_file):
    with open(config_file) as f:
        return json.load(f)


webcams = load_config(".config.json").get("webcams")

for webcam in webcams:
    print(webcam.get("url"))
    webcam["streamlink_url"] = streamlink.streams(webcam.get("url"))["best"].url


def store_frame(stream_name, stream_url):
    print("storing frame...")
    stream_name = stream_name.replace(" ", "_")
    # reinitialize on every capture as it seems to be closed after the first read

    cap = cv.VideoCapture(stream_url)
    ret, frame = cap.read()
    print(f"storing image in {stream_name}...")
    cv.imwrite(f"frames/{stream_name}_{datetime.now() }.jpg", frame)
    cap.release()


while True:
    for webcam in webcams:
        print(webcam.get("url"))
        store_frame(webcam.get("name"), webcam.get("streamlink_url"))
    time.sleep(5)
