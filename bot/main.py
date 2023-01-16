#!/usr/bin/env python3
from urllib import response
import requests
import time

# FOR REFERENCE ON WEBEX API: https://developer.webex.com/docs/api/v1/messages

# Get token
try:
    import authData
    TOKEN = authData.access_token
except ImportError:
    print("Missing authData.py module containing the `access_token` variable")
    exit(-1)

# Configue constants
BASE_URL = "https://api.ciscospark.com/v1/"
HEADERS  = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Function declaratins
def request(url: str, **kwargs: any) -> requests.Response:
    return requests.get(
        f"{url}?{'&'.join([key+'='+kwargs[key] for key in kwargs.keys()])}",
        headers=HEADERS
    )

print("starting bot...")
while True:
    recieve_endpoint = BASE_URL + "rooms"
    message_endpoint = BASE_URL + "messages"
    response = request(recieve_endpoint, sortBy="lastactivity")

    if response.status_code == 200:
        update = response.json()

        for item in update["items"]:
            roomID = item["id"]
            messages = request(message_endpoint, roomId=roomID)
            mjson = messages.json()
            
            for message_item in mjson["items"]:
                pass
        # TODO ADD FUNCTIONALITY
        pass
    elif response.status_code == 429: # too many requests
        pass
    else:
        raise ConnectionError(f"got response code: {response.status_code} with data {response.json()}")
    
    time.sleep(response.headers.get("Retry-After", 1)) # if the header retry-after is available use that, otherwhise use 0.5
