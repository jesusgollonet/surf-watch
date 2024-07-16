import streamlink
import cv2 as cv
from dotenv import load_dotenv
import os


load_dotenv()

streams = streamlink.streams(
    os.getenv("STREAM_URL")
    or "hls://devstreaming-cdn.apple.com/videos/streaming/examples/bipbop_4x3/bipbop_4x3_variant.m3u8"
)


cap = cv.VideoCapture(streams["worst"].url)
ret, frame = cap.read()
cv.imshow("frame", frame)
cv.imwrite("frames/w1.jpg", frame)

cap.release()
