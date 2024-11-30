import requests
import time
import json

# Define the URLs and headers
reboot_url = 'http://172.17.166.132/cgi-bin/cfgjsonrpc'
verify_url = 'http://172.17.166.132/cgi-bin/cfgjsonrpc'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'PHPSESSID=4c0cf889653b6adb9971efa73cdd9af0; webeasy-loggedin=true',
    'Origin': 'http://172.17.166.132',
    'Referer': 'http://172.17.166.132/index.html/setting',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

# Reboot payload
reboot_payload = {
    "jsonrpc": "2.0",
    "method": "set",
    "params": {
        "parameters": [
            {
                "id": "86^@i",
                "type": "integer",
                "name": "button",
                "value": 1
            }
        ]
    },
    "id": 5
}

# Verify payload
verify_payload = {
    "jsonrpc": "2.0",
    "method": "get",
    "params": {
        "parameters": [
            {
                "id": "3501.2^@s",
                "type": "json",
                "name": "Encoder Info"
            },
            {
                "id": "3501.3^@s",
                "type": "json",
                "name": "Encoder Info"
            }
        ]
    },
    "id": 69
}

def reboot_xps():
    response = requests.post(reboot_url, headers=headers, json=reboot_payload)
    if response.status_code == 200:
        print("Reboot command sent successfully.")
    else:
        print(f"Failed to send reboot command. Status code: {response.status_code}")
        print(response.text)

def verify_paths():
    response = requests.post(verify_url, headers=headers, json=verify_payload)
    if response.status_code == 200:
        data = response.json()
        print("Response from server:", json.dumps(data, indent=4))  # Debugging line to print the response
        paths = data.get('result', {}).get('parameters', [])
        all_connected = True
        for path in paths:
            destinations = path.get('value', {}).get('html', {}).get('destination', [])
            for destination in destinations:
                connection_status = destination.get('connection_status')
                if connection_status == 1:
                    print(f"Path {path['id']} with destination {destination['ip_address']}:{destination['port_num']} is connected.")
                else:
                    print(f"Path {path['id']} with destination {destination['ip_address']}:{destination['port_num']} is not connected.")
                    all_connected = False
        if all_connected:
            print("All paths are connected.")
        else:
            print("Some paths are not connected.")
    else:
        print(f"Failed to verify paths. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    while True:
        reboot_xps()
        print("Waiting for 6 minutes to ensure the XPS powers up...")
        time.sleep(360)  # Wait for 6 minutes
        verify_paths()
        print("Waiting for 10 minutes before the next iteration...")
        time.sleep(600)  # Wait for 10 minutes before the next iteration
