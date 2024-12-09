import subprocess
import time
import json

# Define the base URL and common headers
BASE_URL = "https://172.16.136.24/api/v1"
COMMON_HEADERS = [
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9zZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI4MzUwLCJleHAiOjE3MzMzMjg2NTB9.e7QaxEIDt7l7KoiTC_eRhWdfTrNUZYk-AVyBbh_HmiU",
    "-H", "Connection: keep-alive",
    "-H", "Content-Type: application/json",
    "-H", "Cookie: refresh=$2a$10$voeGpDweUuZuZDye5YpicOrgVfUbqTjd37fuISD2XbSSzdObO0E56; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24",
    "-H", "Sec-Fetch-Dest: empty",
    "-H", "Sec-Fetch-Mode: cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "-H", "sec-ch-ua: \"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "-H", "sec-ch-ua-mobile: ?0",
    "-H", "sec-ch-ua-platform: \"Windows\"",
    "--insecure"
]

# Function to execute a cURL command
def execute_curl_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

# Function to create, enable, start, or delete an input/output/flow
def manage_entity(entity_type, entity_id, action, data=None):
    url = f"{BASE_URL}/{entity_type}/"
    if action in ["enable", "start"]:
        url += f"{entity_id}/{action}"
        method = "POST"
    elif action == "delete":
        url += f"{entity_id}"
        method = "DELETE"
    else:
        method = "POST"
    
    cmd = ["curl", url, "-X", method] + COMMON_HEADERS
    if data:
        cmd += ["--data-raw", json.dumps(data)]
    result = execute_curl_command(cmd)
    print(result.stdout)
    print(result.stderr)
    return result

# Function to fetch and parse capability details
def fetch_and_parse_capability():
    cmd = ["curl", f"{BASE_URL}/capability"] + COMMON_HEADERS
    result = execute_curl_command(cmd)
    if result.returncode == 0:
        try:
            data = json.loads(result.stdout)
            for firmware in data.get("firmware", []):
                if firmware.get("softwareName") == "reflektor-bundle":
                    print("Software Name:", firmware.get("softwareName"))
                    print("Software Version:", firmware.get("softwareVersion"))
                    for package in firmware.get("softwarePackages", []):
                        if package.get("packageName") in ["reflektor-api", "reflektor-firmware", "reflektor-user-interface"]:
                            print("Package Name:", package.get("packageName"))
                            print("Version:", package.get("version"))
                            print("Description:", package.get("description"))
        except json.JSONDecodeError:
            print("Failed to parse JSON response")
    else:
        print("Failed to fetch capability details")

# Function to fetch and parse system status
def fetch_and_parse_system_status():
    cmd = ["curl", f"{BASE_URL}/system/status"] + COMMON_HEADERS
    result = execute_curl_command(cmd)
    if result.returncode == 0:
        try:
            data = json.loads(result.stdout)
            cpu_usage = data.get("platform", {}).get("cpuInfo", {}).get("cpuUsage")
            memory_info = data.get("platform", {}).get("memoryInfo", {})
            memory_usage = memory_info.get("memoryUsage")
            memory_total = memory_info.get("memoryTotal")
            memory_free = memory_info.get("memoryFree")
            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {memory_usage}")
            print(f"Memory Total: {memory_total}")
            print(f"Memory Free: {memory_free}")
        except json.JSONDecodeError:
            print("Failed to parse JSON response")
    else:
        print("Failed to fetch system status")

# Main loop to execute the commands 50 times
for i in range(2000):
    print("")
    print(f"Iteration {i+1}:")

    # Step 1: Create the input
    print("Creating input...")
    manage_entity("inputs", "", "create", {
        "inputId": "srt-in",
        "inputAliasName": "srt-in",
        "InputMode": "SRT",
        "tsMonitorControl": True,
        "config": {
            "srt": {
                "srtConfig": {
                    "Mode": "LISTENER",
                    "ipAddress": "172.16.0.0",
                    "port": 1234,
                    "interface": "eth2",
                    "latency": 100,
                    "sourcePortMode": False,
                    "streamId": "",
                    "encryptionControl": False
                }
            }
        }
    })

    time.sleep(2)
    # Step 2: Enable the input
    print("Enabling input...")
    manage_entity("inputs", "srt-in", "enable")
    time.sleep(2)
    # Step 3: Start the input
    print("Starting input...")
    manage_entity("inputs", "srt-in", "start")

    # Step 4: Create the output
    print("Creating output...")
    manage_entity("outputs", "", "create", {
        "outputId": "srt-out",
        "outputAliasName": "srt-out",
        "OutputMode": "SRT",
        "inputs": ["srt-in"],
        "processingUnits": [],
        "tsMonitorControl": True,
        "config": {
            "srt": {
                "srtConfig": {
                    "Mode": "CALLER",
                    "ipAddress": "172.16.0.0",
                    "port": 1234,
                    "interface": "eth2",
                    "latency": 100,
                    "sourcePortMode": False,
                    "streamId": "",
                    "encryptionControl": False,
                    "outputTtl": 100
                },
                "maxOutputBitrate": 60000
            }
        }
    })

    time.sleep(2)
    # Step 5: Enable the output
    print("Enabling output...")
    manage_entity("outputs", "srt-out", "enable")
    
    time.sleep(2)
    # Step 6: Start the output
    print("Starting output...")
    manage_entity("outputs", "srt-out", "start")

    # Step 7: Create the flow
    print("Creating flow...")
    manage_entity("flows", "", "create", {
        "flowId": "flow-srt",
        "flowAliasName": "flow-srt",
        "inputs": ["srt-in"],
        "processingUnits": [],
        "outputs": ["srt-out"]
    })
    time.sleep(2)
    # Step 8: Enable the flow
    print("Enabling flow...")
    manage_entity("flows", "flow-srt", "enable")
    
    time.sleep(2)
    # Step 9: Start the flow
    print("Starting flow...")
    manage_entity("flows", "flow-srt", "start")
    time.sleep(2)

    # Step 11: Delete the flow
    print("Deleting flow...")
    manage_entity("flows", "flow-srt", "delete")
    time.sleep(2)

    # Step 13: Fetch and parse capability details
    fetch_and_parse_capability()
    time.sleep(2)

    # Step 14: Fetch and parse system status
    fetch_and_parse_system_status()
    time.sleep(2)
print("Completed 2000 iterations.")
