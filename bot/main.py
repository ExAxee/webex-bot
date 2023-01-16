#!/usr/bin/env python3
from urllib import response
import requests
import json

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

print("starting bot...")
while True:
    endpoint = BASE_URL + "rooms?sortBy=lastactivity"
    response = requests.get(endpoint, headers=HEADERS)

    if response.status_code == 200:
        # TODO ADD FUNCTIONALITY
        pass
    else:
        raise ConnectionError(f"got response code: {response.status_code} with data {response.json()}")
