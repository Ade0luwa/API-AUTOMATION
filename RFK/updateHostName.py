import requests
import time
import json
import urllib3

# Suppress only the single InsecureRequestWarning from urllib3 needed for this script
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_new_token():
    url = "https://172.16.151.226/api/v1/login"
    headers = {
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": "",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "refresh=$2a$10$QuX.rUPbFcjMHaPPnpWwI.7D7P0JNgUQCnm0X4gKi.PIw4cvLS/ri",
        "Origin": "https://172.16.151.226",
        "Referer": "https://172.16.151.226/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "authentication-type": "DB",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }
    payload = {
        "username": "admin",
        "password": "admin"
    }
    response = requests.post(url, headers=headers, json=payload, verify=False)
    print(f"Token response: {response.status_code} {response.text}")
    if response.status_code == 200:
        return response.text.strip('"')  # Remove any surrounding quotes
    else:
        raise Exception("Failed to get token")

def update_hostname(token, new_hostname):
    url = "https://172.16.151.226/api/v1/system"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "generalSettings": {
            "platform": {
                "hostName": new_hostname
            }
        }
    }
    # print(f"Update hostname request headers: {headers}")
    print(f"Update hostname request payload: {json.dumps(payload)}")
    response = requests.patch(url, headers=headers, json=payload, verify=False)
    print(f"Update hostname response: {response.status_code}, {response.text}")
    return response.status_code == 200

def verify_hostname(token, expected_hostname):
    url = "https://172.16.151.226/api/v1/system"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, verify=False)
    print(f"Verify hostname response: {response.status_code}, {response.text}")
    if response.status_code == 200:
        current_hostname = response.json().get("generalSettings", {}).get("platform", {}).get("hostName")
        return current_hostname == expected_hostname
    else:
        print("Error verifying hostname:", response.text)
        return False

# Main script
special_characters = ["--", "---"]
base_hostname = "evertz123"

try:
    for iteration in range(50):
        print(f"Iteration {iteration + 1}")
        token = get_new_token()
        if token:
            for i, char in enumerate(special_characters):
                new_hostname = f"{base_hostname}{char}test"
                print(f"Updating hostname to: {new_hostname}")
                if update_hostname(token, new_hostname):
                    time.sleep(120)
                    if verify_hostname(token, new_hostname):
                        print(f"Hostname successfully updated to: {new_hostname}")
                    else:
                        print(f"Failed to verify hostname: {new_hostname}")
                else:
                    print(f"Failed to update hostname: {new_hostname}")
        else:
            print("Failed to get token")
except Exception as e:
    print(e)
