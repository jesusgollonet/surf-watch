import requests
import streamlink
import cv2 as cv
from datetime import datetime
import sys
import os

# Add the parent directory of 'lib' to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# url = "https://www.skylinewebcams.com/en/webcam/espana/andalucia/cadiz/el-puerto-de-santa-maria.html"
# url = "https://www.skylinewebcams.com/es/webcam/espana/andalucia/cadiz/el-puerto-de-santa-maria-puerto-sherry.html"
# url = "https://www.skylinewebcams.com/es/webcam/espana/andalucia/cadiz/puerto-conil-de-la-frontera.html"
url = (
    "https://www.skylinewebcams.com/es/webcam/espana/andalucia/casares/playa-ancha.html"
)


def retrieve_session_id(url):
    response = requests.get(url)

    php_sess_id = None
    # Check if the request was successful
    if response.status_code == 200:
        # Extract cookies from the response
        cookies = response.cookies
        # Print out the PHP session ID if it exists
        php_sess_id = cookies.get("PHPSESSID") if "PHPSESSID" in cookies else None
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return php_sess_id


def capture_frame(m3u8_url):
    streams = streamlink.streams(m3u8_url)
    stream = streams["best"]

    cap = cv.VideoCapture(stream.url)
    ret, frame = cap.read()
    stream_name = f"test_{datetime.now()}"
    print(f"storing image in {stream_name}...")
    cv.imwrite(f"frames/{stream_name}_{datetime.now() }.jpg", frame)
    cap.release()


session_id = retrieve_session_id(url)
stream_url = f"https://hd-auth.skylinewebcams.com/live.m3u8?a={session_id}"
capture_frame(stream_url)
