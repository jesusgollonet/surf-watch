# in order to import a frame from sw, we need to

# 1. visit the website
# 2. extract the session id
# 3. append it to the stream url
# 4. capture the frame
# 5. store it in a file


def get_sw_stream_url_for_page(sw_page_url):
    session_id = _retrieve_session_id(sw_page_url)
    if session_id is None:
        print("Failed to retrieve the PHP session ID")
        return None
    else:
        return f"https://hd-auth.skylinewebcams.com/live.m3u8?a={session_id}"


def _retrieve_session_id(url):
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
