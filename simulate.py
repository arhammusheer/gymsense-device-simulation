import requests
import random
import os
import json

# Fetching URL and credentials from environment variables
url = os.getenv('GYMSENSE_URL')
hub_id = os.getenv('HUB_ID')
hub_key = os.getenv('HUB_KEY')
device_id = os.getenv('DEVICE_ID')
device_key = os.getenv('DEVICE_KEY')

def simulate_battery_depletion(old_battery_level):
    # Simulate battery depletion
    battery_level = old_battery_level*1000 # For integer division
    battery_level -= random.randint(0, 10)  # Simulate battery drain
    battery_level = max(battery_level, 0)  # Ensure battery level is not negative
    battery_level /= 1000  # Convert back to float

    return battery_level

def flip_old_occupancy(old_occupancy):
    return not old_occupancy


def send_update(url, hub_id, hub_key, device_id, device_key, old_battery_level, old_occupancy):
    should_send_update = random.choice([True, False])

    if should_send_update:
        # Simulate battery depletion
        battery_level = simulate_battery_depletion(old_battery_level)

        # Simulate occupancy
        occupancy = flip_old_occupancy(old_occupancy)


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
            json_response = response.json()
            print(json.dumps(json_response, indent=2))
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.json())  # Optionally print the response text to understand what went wrong
            print("Debug")
            for history in response.history:
                print(history.status_code, history.url, history.text)

        return battery_level, occupancy
    else:
        print("No update sent this time.")
        return old_battery_level, old_occupancy

def check_env():
    if not all([url, hub_id, hub_key, device_id, device_key]):
        print("Error: One or more required environment variables are missing.")
        print("Make sure GYMSENSE_URL, HUB_ID, HUB_KEY, DEVICE_ID, and DEVICE_KEY are set.")
        exit(1)

def send(old_battery_level, old_occupancy):
    return send_update(url, hub_id, hub_key, device_id, device_key, old_battery_level, old_occupancy)

if __name__ == "__main__":
    check_env()
    send()