import streamlink
import cv2 as cv
from dotenv import load_dotenv
import os
import time
from datetime import datetime


load_dotenv()

streams = streamlink.streams(
    os.getenv("STREAM_URL")
    or "hls://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8"
)


def store_frame():
    print("storing frame...")
    cap = cv.VideoCapture(
        streams["worst"].url
    )  # reinitialize on every capture as it seems to be closed after the first read
    ret, frame = cap.read()
    cv.imwrite(f"frames/{datetime.now() }.jpg", frame)
    cap.release()


while True:
    store_frame()
    print("waiting 5 seconds...")
    time.sleep(5)
