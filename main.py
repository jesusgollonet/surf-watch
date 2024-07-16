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
# cv.destroyAllWindows()


# fd = streams["best"].open()
# data = fd.read(1024)
# # save the data to a file

# c = 0
# with open("output.ts", "wb") as f:
# while data and c < 1000:
# f.write(data)
# data = fd.read(1024)
# c += 1

# fd.close()
