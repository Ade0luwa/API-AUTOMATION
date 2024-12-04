import subprocess
import time

# Define the cURL commands for input
create_input_cmd = [
    "curl", "https://172.16.136.24/api/v1/inputs/",
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI4MzUwLCJleHAiOjE3MzMzMjg2NTB9.e7QaxEIDt7l7KoiTC_eRhWdfTrNUZYk-AVyBbh_HmiU",
    "-H", "Connection: keep-alive",
    "-H", "Content-Type: application/json",
    "-H", "Cookie: refresh=$2a$10$voeGpDweUuZuZDye5YpicOrgVfUbqTjd37fuISD2XbSSzdObO0E56; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24/Sources",
    "-H", "Sec-Fetch-Dest: empty",
    "-H", "Sec-Fetch-Mode: cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "-H", "sec-ch-ua: \"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "-H", "sec-ch-ua-mobile: ?0",
    "-H", "sec-ch-ua-platform: \"Windows\"",
    "--data-raw", "{\"inputId\":\"srt-in\",\"inputAliasName\":\"srt-in\",\"InputMode\":\"SRT\",\"tsMonitorControl\":true,\"config\":{\"srt\":{\"srtConfig\":{\"Mode\":\"LISTENER\",\"ipAddress\":\"172.16.0.0\",\"port\":1234,\"interface\":\"eth2\",\"latency\":100,\"sourcePortMode\":false,\"streamId\":\"\",\"encryptionControl\":false}}}}",
    "--insecure"
]

enable_input_cmd = [
    "curl", "https://172.16.136.24/api/v1/inputs/srt-in/enable",
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI4MzM5LCJleHAiOjE3MzMzMjg2Mzl9.iiULxLgyM6X1DwwiuBk4pqxLfPZv-9dp2dLa6Rm0Si8",
    "-H", "Connection: keep-alive",
    "-H", "Content-Type: application/json",
    "-H", "Cookie: refresh=$2a$10$voeGpDweUuZuZDye5YpicOrgVfUbqTjd37fuISD2XbSSzdObO0E56; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24/Sources",
    "-H", "Sec-Fetch-Dest: empty",
    "-H", "Sec-Fetch-Mode: cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "-H", "sec-ch-ua: \"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "-H", "sec-ch-ua-mobile: ?0",
    "-H", "sec-ch-ua-platform: \"Windows\"",
    "--data-raw", "{}",
    "--insecure"
]

start_input_cmd = [
    "curl", "https://172.16.136.24/api/v1/inputs/srt-in/start",
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI4MzM5LCJleHAiOjE3MzMzMjg2Mzl9.iiULxLgyM6X1DwwiuBk4pqxLfPZv-9dp2dLa6Rm0Si8",
    "-H", "Connection: keep-alive",
    "-H", "Content-Type: application/json",
    "-H", "Cookie: refresh=$2a$10$voeGpDweUuZuZDye5YpicOrgVfUbqTjd37fuISD2XbSSzdObO0E56; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24/Sources",
    "-H", "Sec-Fetch-Dest: empty",
    "-H", "Sec-Fetch-Mode: cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "-H", "sec-ch-ua: \"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "-H", "sec-ch-ua-mobile: ?0",
    "-H", "sec-ch-ua-platform: \"Windows\"",
    "--data-raw", "{}",
    "--insecure"
]

# Define the cURL commands for output
create_output_cmd = [
    "curl", "https://172.16.136.24/api/v1/outputs/",
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI4MzUwLCJleHAiOjE3MzMzMjg2NTB9.e7QaxEIDt7l7KoiTC_eRhWdfTrNUZYk-AVyBbh_HmiU",
    "-H", "Connection: keep-alive",
    "-H", "Content-Type: application/json",
    "-H", "Cookie: refresh=$2a$10$voeGpDweUuZuZDye5YpicOrgVfUbqTjd37fuISD2XbSSzdObO0E56; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24/Destinations",
    "-H", "Sec-Fetch-Dest: empty",
    "-H", "Sec-Fetch-Mode: cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "-H", "sec-ch-ua: \"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "-H", "sec-ch-ua-mobile: ?0",
    "-H", "sec-ch-ua-platform: \"Windows\"",
    "--data-raw", "{\"outputId\":\"srt-out\",\"outputAliasName\":\"srt-out\",\"OutputMode\":\"SRT\",\"inputs\":[\"srt-in\"],\"processingUnits\":[],\"tsMonitorControl\":true,\"config\":{\"srt\":{\"srtConfig\":{\"Mode\":\"CALLER\",\"ipAddress\":\"172.16.0.0\",\"port\":1234,\"interface\":\"eth2\",\"latency\":100,\"sourcePortMode\":false,\"streamId\":\"\",\"encryptionControl\":false,\"outputTtl\":100},\"maxOutputBitrate\":60000}}}",
    "--insecure"
]

enable_output_cmd = [
    "curl", "https://172.16.136.24/api/v1/outputs/srt-out/enable",
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI4MzM5LCJleHAiOjE3MzMzMjg2Mzl9.iiULxLgyM6X1DwwiuBk4pqxLfPZv-9dp2dLa6Rm0Si8",
    "-H", "Connection: keep-alive",
    "-H", "Content-Type: application/json",
    "-H", "Cookie: refresh=$2a$10$voeGpDweUuZuZDye5YpicOrgVfUbqTjd37fuISD2XbSSzdObO0E56; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24/Destinations",
    "-H", "Sec-Fetch-Dest: empty",
    "-H", "Sec-Fetch-Mode: cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "-H", "sec-ch-ua: \"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "-H", "sec-ch-ua-mobile: ?0",
    "-H", "sec-ch-ua-platform: \"Windows\"",
    "--data-raw", "{}",
    "--insecure"
]

start_output_cmd = [
    "curl", "https://172.16.136.24/api/v1/outputs/srt-out/start",
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI4MzM5LCJleHAiOjE3MzMzMjg2Mzl9.iiULxLgyM6X1DwwiuBk4pqxLfPZv-9dp2dLa6Rm0Si8",
    "-H", "Connection: keep-alive",
    "-H", "Content-Type: application/json",
    "-H", "Cookie: refresh=$2a$10$voeGpDweUuZuZDye5YpicOrgVfUbqTjd37fuISD2XbSSzdObO0E56; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24/Destinations",
    "-H", "Sec-Fetch-Dest: empty",
    "-H", "Sec-Fetch-Mode: cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "-H", "sec-ch-ua: \"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "-H", "sec-ch-ua-mobile: ?0",
    "-H", "sec-ch-ua-platform: \"Windows\"",
    "--data-raw", "{}",
    "--insecure"
]

# Define the cURL commands for flow
create_flow_cmd = [
    "curl", "https://172.16.136.24/api/v1/flows/",
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI0Njc0LCJleHAiOjE3MzMzMjQ5NzR9.vGLrzOa2yN42-RGZHr8kyaCvVTb7CIWbqjRULwtuXrc",
    "-H", "Connection: keep-alive",
    "-H", "Content-Type: application/json",
    "-H", "Cookie: refresh=$2a$10$r1aduiYlBQ7RXMulBWzCk.s6NE6NPRmk6sljgKckANJgm2m2DGckW; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24/Flows",
    "-H", "Sec-Fetch-Dest: empty",
    "-H", "Sec-Fetch-Mode: cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "-H", "sec-ch-ua: \"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "-H", "sec-ch-ua-mobile: ?0",
    "-H", "sec-ch-ua-platform: \"Windows\"",
    "--data-raw", "{\"flowId\":\"flow-srt\",\"flowAliasName\":\"flow-srt\",\"inputs\":[\"srt-in\"],\"processingUnits\":[],\"outputs\":[\"srt-out\"]}",
    "--insecure"
]

enable_flow_cmd = [
    "curl", "https://172.16.136.24/api/v1/flows/flow-srt/enable",
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI0MDk3LCJleHAiOjE3MzMzMjQzOTd9.zep75sJDmETxuWIzfFyYeWIzirk3aBaFPAAzvOzvQKQ",
        "-H", "Connection: keep-alive",
    "-H", "Content-Type: application/json",
    "-H", "Cookie: refresh=$2a$10$r1aduiYlBQ7RXMulBWzCk.s6NE6NPRmk6sljgKckANJgm2m2DGckW; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24/Flows",
    "-H", "Sec-Fetch-Dest: empty",
    "-H", "Sec-Fetch-Mode: cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "-H", "sec-ch-ua: \"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "-H", "sec-ch-ua-mobile: ?0",
    "-H", "sec-ch-ua-platform: \"Windows\"",
    "--data-raw", "{}",
    "--insecure"
]

start_flow_cmd = [
    "curl", "https://172.16.136.24/api/v1/flows/flow-srt/start",
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI0MDk3LCJleHAiOjE3MzMzMjQzOTd9.zep75sJDmETxuWIzfFyYeWIzirk3aBaFPAAzvOzvQKQ",
    "-H", "Connection: keep-alive",
    "-H", "Content-Type: application/json",
    "-H", "Cookie: refresh=$2a$10$r1aduiYlBQ7RXMulBWzCk.s6NE6NPRmk6sljgKckANJgm2m2DGckW; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24/Flows",
    "-H", "Sec-Fetch-Dest: empty",
    "-H", "Sec-Fetch-Mode: cors",
    "-H", "Sec-Fetch-Site: same-origin",
    "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
    "-H", "sec-ch-ua: \"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "-H", "sec-ch-ua-mobile: ?0",
    "-H", "sec-ch-ua-platform: \"Windows\"",
    "--data-raw", "{}",
    "--insecure"
]

delete_flow_cmd = [
    "curl", "https://172.16.136.24/api/v1/flows/flow-srt",
    "-X", "DELETE",
    "-H", "Accept: application/json",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZXMiOlsiYWRtaW4iLCJ3cml0ZSIsInJlYWQiXSwiaWF0IjoxNzMzMzI0OTQ0LCJleHAiOjE3MzMzMjUyNDR9.ipXqGrd_4ReoL__5jUpEa_K88gjEp3XyDdvxXZd5xBM",
    "-H", "Connection: keep-alive",
    "-H", "Cookie: refresh=$2a$10$r1aduiYlBQ7RXMulBWzCk.s6NE6NPRmk6sljgKckANJgm2m2DGckW; PHPSESSID=gm3n2v8r7o308f0a2gncpvmish",
    "-H", "Origin: https://172.16.136.24",
    "-H", "Referer: https://172.16.136.24/Flows",
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
    print(result.stdout)
    print(result.stderr)
    return result

# Main loop to execute the commands 50 times
for i in range(50):
    print(f"Iteration {i+1}:")

    # Step 1: Create the input
    print("Creating input...")
    execute_curl_command(create_input_cmd)

    # Step 2: Enable the input
    print("Enabling input...")
    execute_curl_command(enable_input_cmd)

    # Step 3: Start the input
    print("Starting input...")
    execute_curl_command(start_input_cmd)

    # Step 4: Create the output
    print("Creating output...")
    execute_curl_command(create_output_cmd)

    # Step 5: Enable the output
    print("Enabling output...")
    execute_curl_command(enable_output_cmd)

    # Step 6: Start the output
    print("Starting output...")
    execute_curl_command(start_output_cmd)

    # Step 7: Create the flow
    print("Creating flow...")
    execute_curl_command(create_flow_cmd)

    # Step 8: Enable the flow
    print("Enabling flow...")
    execute_curl_command(enable_flow_cmd)

    # Step 9: Start the flow
    print("Starting flow...")
    execute_curl_command(start_flow_cmd)

    # Step 10: Wait for 15 seconds
    print("Waiting for 15 seconds...")
    time.sleep(15)

    # Step 11: Delete the flow
    print("Deleting flow...")
    execute_curl_command(delete_flow_cmd)

    # Step 12: Wait for 15 seconds
    print("Waiting for 15 seconds...")
    time.sleep(15)

print("Completed 50 iterations.")

