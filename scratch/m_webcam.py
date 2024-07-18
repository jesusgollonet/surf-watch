import cv2 as cv
from streamlink import Streamlink
import numpy as np
import tempfile

temp_file = tempfile.NamedTemporaryFile(delete=False)
temp_file_name = temp_file.name
print(temp_file_name)

url = "https://livecams.meteo365.es/hls_live/misericordia.m3u8"

session = Streamlink(options={"http-headers": "Referer=https://meteo365.es/"})
streams = session.streams(url)

print(streams)
fd = streams["worst"].open()
# Read the data in chunks until we get a complete frame
# Write the stream data to the temporary file
c = 0
while True and c < 200:
    chunk = fd.read(1024)
    if not chunk:
        break
    temp_file.write(chunk)
    print(c)
    c += 1
fd.close()
temp_file.close()
# Open the temporary file with OpenCV
cap = cv.VideoCapture(temp_file_name)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Read a frame to determine the shape
ret, frame = cap.read()

if ret:
    print("Frame shape:", frame.shape)  # (height, width, channels)
    # Save the frame as an image if needed
    cv.imwrite("frame.jpg", frame)
    print("Image saved as frame.jpg")
else:
    print("Error: Could not read frame from the stream.")

cap.release()
