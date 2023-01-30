#!/usr/bin/env python3
from utils import post, request
from constants import BASE_URL
from datetime import datetime
import time

# FOR REFERENCE ON WEBEX API: https://developer.webex.com/docs/api/v1/messages

# configure last update
LAST_UPDATE = datetime.now()

print("starting bot...")
while True:
    recieve_endpoint = BASE_URL + "rooms"
    message_endpoint = BASE_URL + "messages"

    # get last udpates
    messageUpdate = request(recieve_endpoint, sortBy="lastactivity")

    if messageUpdate.status_code == 200:
        # get response in json format
        update = messageUpdate.json()

        # cycle throught update items (basically a list of rooms with recent activity)
        for item in update["items"]:
            roomID = item["id"]

            # get the messages in the given room
            messages = request(message_endpoint, roomId=roomID)
            mjson = messages.json()
            
            # cycle through messages in the room
            for message_item in mjson["items"]:
                # if message is sent before the last update then ignore it
                if LAST_UPDATE < datetime.strptime(message_item["created"], "%Y-%m-%dT%H:%M:%S.%fZ"):
                    continue

                # if the message is a direct message then respond directly
                if message_item["roomType"] == "direct":
                    postResponse = post(
                        message_endpoint,
                        roomId = message_item["roomId"],
                        toPersonId = message_item["personId"],
                        text = "da funzia"
                    )
                else:
                    postResponse = post(
                        message_endpoint,
                        roomId = message_item["roomId"],
                        text = "da funzia"
                    )
    elif messageUpdate.status_code == 429: # too many requests
        pass
    else:
        raise ConnectionError(f"got response code: {messageUpdate.status_code} with data {messageUpdate.json()}")
    
    LAST_UPDATE = datetime.now()
    
    time.sleep(messageUpdate.headers.get("Retry-After", 1)) # if the header retry-after is available use that, otherwhise use 0.5
