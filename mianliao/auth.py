import requests
import os
import json
from pyquery import PyQuery as pq
import getpass

"""
A Helper Script to auth the uestc-mianliao wifi
"""

print("""
   _____  .__              .__  .__
  /     \ |__|____    ____ |  | |__|____    ____
 /  \ /  \|  \__  \  /    \|  | |  \__  \  /  _ \\
/    Y    \  |/ __ \|   |  \  |_|  |/ __ \(  <_> )
\____|__  /__(____  /___|  /____/__(____  /\____/
        \/        \/     \/             \/
""")

requests.packages.urllib3.disable_warnings()

pass_path = os.path.expanduser("~/.cache/mianliao_auth.json")
r = requests.session()
ua = "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0"
r.headers['User-Agent'] = ua

os.makedirs(os.path.split(pass_path)[0], exist_ok=True)

if os.path.exists(pass_path):
    with open(pass_path) as fp:
        data = json.load(fp)
else:
    data = {}
    data["username"] = input("Username: ")
    data['password'] = getpass.getpass()

r.post('https://wifi.52mianliao.com', data={'ua':ua, 'sh': 720, 'sw':1366, 'ww': 1330, 'wh': 600}, verify=False)
r.post("https://wifi.52mianliao.com/", data={
    "action": "login",
    "username": data["username"],
    "password": data["password"]
}, verify=False)
rc = r.post('https://wifi.52mianliao.com', data={'ua':ua, 'sh': 720, 'sw':1366, 'ww': 1330, 'wh': 600}, verify=False).content.decode()
if "登陆用户" in rc:
    p = pq(rc)
    # success
    print("\n".join([i.text for i in p("label")]))
    with open(pass_path, 'w') as fp:
        json.dump(data, fp)
else:
    print("Login Failed.......")
