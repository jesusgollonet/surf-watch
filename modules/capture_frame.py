import streamlink
import cv2 as cv
from datetime import datetime


def capture_frame(m3u8_url, stream_name):
    streams = streamlink.streams(m3u8_url)
    stream = streams["best"]
    cap = cv.VideoCapture(stream.url)
    ret, frame = cap.read()
    print(f"storing image in {stream_name}...")
    cv.imwrite(f"frames/{stream_name}_{datetime.now() }.jpg", frame)
    cap.release()
