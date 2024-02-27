import requests
import random
import os

# Fetching URL and credentials from environment variables
url = os.getenv('GYMSENSE_URL')
hub_id = os.getenv('HUB_ID')
hub_key = os.getenv('HUB_KEY')
device_id = os.getenv('DEVICE_ID')
device_key = os.getenv('DEVICE_KEY')

# Check if all required environment variables are set
if not all([url, hub_id, hub_key, device_id, device_key]):
    print("Error: One or more required environment variables are missing.")
    print("Make sure GYMSENSE_URL, HUB_ID, HUB_KEY, DEVICE_ID, and DEVICE_KEY are set.")
else:
    # Decide randomly whether to send an update
    should_send_update = random.choice([True, False])

    if should_send_update:
        battery_level = random.randint(20, 100)  # Randomize for each run for simulation
        occupancy = random.choice([True, False])  # Generate random occupancy

        # Prepare the data payload
        data = {
            "hub_id": hub_id,
            "hub_key": hub_key,
            "id": device_id,
            "key": device_key,
            "battery_level": battery_level,
            "occupancy": occupancy
        }

        # Send the POST request
        response = requests.post(url, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            print("Request successful!")
            print(response.json())  # Optionally print the response data
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)  # Optionally print the response text to understand what went wrong
    else:
        print("No update sent this time.")
