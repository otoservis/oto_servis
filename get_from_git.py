import requests
import json
from urllib.request import urlretrieve

url = "https://raw.githubusercontent.com/otoservis/oto_servis/main/version.json"
versions = json.loads(requests.get(url).text)

print(versions)
current_os = "win_10_64"
current_version = 0
latest_version = versions[current_os]

if current_version != latest_version:
    print("new version available. Downloading {} version".format(latest_version))
    exe_url = "https://raw.githubusercontent.com/otoservis/oto_servis/main/{}/{}/oto_servis_{}.exe".format(current_os, latest_version, current_os)
    filename = "oto_servis_{}.exe".format(current_os, latest_version, current_os)
    urlretrieve(exe_url, filename)
    print("download is done")    
