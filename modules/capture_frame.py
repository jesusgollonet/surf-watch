import streamlink as sl
import tempfile
import cv2 as cv
from datetime import datetime


def capture_frame(m3u8_url, stream_name):
    if "meteo365" in m3u8_url:
        _capture_frame_m(m3u8_url, stream_name)
    else:
        _capture_frame(m3u8_url, stream_name)


def _capture_frame(m3u8_url, stream_name):
    streams = sl.streams(m3u8_url)
    stream = streams["best"]
    cap = cv.VideoCapture(stream.url)
    ret, frame = cap.read()
    print(f"storing image in {stream_name}...")
    cv.imwrite(f"frames/{stream_name}_{datetime.now() }.jpg", frame)
    cap.release()


def _capture_frame_m(m3u8_url, stream_name):
    session = sl.Streamlink(options={"http-headers": "Referer=https://meteo365.es/"})
    streams = session.streams(m3u8_url)
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_name = temp_file.name

    fd = streams["best"].open()
    c = 0
    while True and c < 200:
        chunk = fd.read(1024)
        if not chunk:
            break
        temp_file.write(chunk)
        c += 1
    fd.close()
    temp_file.close()
    cap = cv.VideoCapture(temp_file_name)
    ret, frame = cap.read()
    print(f"storing image in {stream_name}...")
    cv.imwrite(f"frames/{stream_name}_{datetime.now() }.jpg", frame)
    cap.release()
