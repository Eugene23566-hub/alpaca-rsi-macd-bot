import requests
import os

def check_for_update():
    url = 'https://your-updates-server.com/bot_upgrade.zip'
    r = requests.get(url)
    with open("upgrade.zip", "wb") as f:
        f.write(r.content)
    os.system("unzip -o upgrade.zip -d ./")
    print("[INFO] Bot updated.")
