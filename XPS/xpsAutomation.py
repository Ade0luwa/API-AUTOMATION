import requests
import json
import time
from datetime import datetime
import random
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'http://172.17.244.71/cgi-bin/cfgjsonrpc'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Session a03fffb3c14da7cb724c231c16bde489',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'PHPSESSID=a03fffb3c14da7cb724c231c16bde489; webeasy-loggedin=true',
    'Origin': 'http://172.17.244.71',
    'Referer': 'http://172.17.244.71/page12.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'X-Requested-With': 'XMLHttpRequest'
}

def validate_set_values(expected_values, decoder_id):
    fetch_data = {
        "jsonrpc": "2.0",
        "method": "get",
        "params": {
            "parameters": [
                {"id": f"231.{decoder_id}^@i", "type": "integer", "name": "Mode"},
                {"id": f"207.{decoder_id}^@s", "type": "string", "name": "Address"},
                {"id": f"229.{decoder_id}^@s", "type": "string", "name": "Remote Address"},
                {"id": f"208.{decoder_id}^@i", "type": "integer", "name": "Port"},
                {"id": f"209.{decoder_id}^@i", "type": "integer", "name": "Input Interface-equivalent control for REST API"},
                {"id": f"290.{decoder_id}^@i", "type": "integer", "name": "Source Port Mode"},
                {"id": f"291.{decoder_id}^@i", "type": "integer", "name": "Source Port"},
                {"id": f"296.{decoder_id}^@s", "type": "string", "name": "Stream ID"},
                {"id": f"228.{decoder_id}^@i", "type": "integer", "name": "SRT Latency"}
            ]
        },
        "id": 6,
        "username": "admin"
    }

    response = requests.post(url, headers=headers, data=json.dumps(fetch_data))
    response_time = response.elapsed.total_seconds()
    print(f"Validation Status Code: {response.status_code}, Response Time: {response_time}s, Response: {response.text}")

    if response.status_code != 200:
        print("Validation failed: Non-200 status code")
        return False

    response_json = response.json()
    if 'result' not in response_json or 'parameters' not in response_json['result']:
        print("Validation failed: Invalid response format")
        return False

    fetched_values = {param['id']: param['value'] for param in response_json['result']['parameters']}
    for key, expected_value in expected_values.items():
        if str(fetched_values.get(key)) != str(expected_value):
            print(f"Validation failed: {key} expected {expected_value}, got {fetched_values.get(key)}")
            return False

    return True

total_runs = 13000
decoder1_results = [0, 0, 0, None]  # [total_runs, total_passed, total_failed, execution_time]
decoder2_results = [0, 0, 0, None]  # [total_runs, total_passed, total_failed, execution_time]

start_time = datetime.now()

for i in range(total_runs):
    for decoder_id, results in [(0, decoder1_results), (1, decoder2_results)]:
        input_interface_value = str(i % 2)
        mode_value = i % 2
        source_port_mode_value = str(i % 2)
        srt_latency_value = random.randint(60, 8000)

        params = [
            {
                "id": f"294.{decoder_id}^@s",
                "type": "json",
                "name": "Input Interface",
                "value": {
                    "state": {
                        "value": input_interface_value
                    }
                }
            },
            {
                "id": f"231.{decoder_id}^@i",
                "type": "integer",
                "name": "Mode",
                "value": mode_value
            },
            {
                "id": f"228.{decoder_id}^@i",
                "type": "integer",
                "name": "SRT Latency",
                "value": srt_latency_value
            }
        ]

        expected_values = {
            f"231.{decoder_id}^@i": mode_value,
            f"209.{decoder_id}^@i": input_interface_value,
            f"228.{decoder_id}^@i": srt_latency_value
        }

        if mode_value == 0:
            params.extend([
                {
                    "id": f"207.{decoder_id}^@s",
                    "type": "string",
                    "name": "Address",
                    "value": "10.10.77.61" if decoder_id == 0 else "10.10.10.78"
                },
                {
                    "id": f"208.{decoder_id}^@i",
                    "type": "integer",
                    "name": "Port",
                    "value": 3073
                },
                {
                    "id": f"290.{decoder_id}^@i",
                    "type": "integer",
                    "name": "Source Port Mode",
                    "value": source_port_mode_value
                }
            ])
            expected_values.update({
                f"207.{decoder_id}^@s": "10.10.77.61" if decoder_id == 0 else "10.10.10.78",
                f"208.{decoder_id}^@i": 3073,
                f"290.{decoder_id}^@i": source_port_mode_value
            })

        data = {
            "jsonrpc": "2.0",
            "method": "set",
            "params": {
                "parameters": params
            },
            "id": 25,
            "username": "admin"
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_time = response.elapsed.total_seconds()
        print(f"Iteration {i+1} (Decoder {decoder_id}): Status Code: {response.status_code}, Response Time: {response_time}s, Response: {response.text}")

        results[0] += 1  # Increment total_runs

        if response.status_code != 200:
            print("Set request failed: Non-200 status code")
            results[2] += 1  # Increment total_failed
            continue

        if validate_set_values(expected_values, decoder_id):
            results[1] += 1  # Increment total_passed
        else:
            results[2] += 1  # Increment total_failed

        time.sleep(0.5)

end_time = datetime.now()
execution_time = end_time - start_time

decoder1_results[3] = execution_time
decoder2_results[3] = execution_time

# Print summary
print("\nDecoder 1 Test Summary:")
print(f"Total Runs: {decoder1_results[0]}")
print(f"Total Passed: {decoder1_results[1]}")
print(f"Total Failed: {decoder1_results[2]}")
print(f"Total Execution Time: {decoder1_results[3]}")

print("\nDecoder 2 Test Summary:")
print(f"Total Runs: {decoder2_results[0]}")
print(f"Total Passed: {decoder2_results[1]}")
print(f"Total Failed: {decoder2_results[2]}")
print(f"Total Execution Time: {decoder2_results[3]}")
