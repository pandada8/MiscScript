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
     /  \ /  \|  \__  \  /  _ \|  | |  \__  \  /    \ 
    /    Y    \  |/ __ \(  <_> )  |_|  |/ __ \|   |  \\
    \____|__  /__(____  /\____/|____/__(____  /___|  /
            \/        \/                    \/     \/ """)

pass_path = os.path.expanduser("~/.cache/wifi_auth/config.json") 
r = requests.session()


os.makedirs(os.path.split(pass_path)[0], exist_ok=True)

if os.path.exists(pass_path):
    with open(pass_path) as fp:
        data = json.load(fp)
        rc = r.post("http://wifi.52mianliao.com/", data={
            "action": "login",
            "username": data["username"],
            "password": data["password"]
        }).content.decode()
        p = pq(rc)
        if "登陆用户" in rc:
            # success
            print("\n".join([i.text for i in p("label")]))
        else:
            print("Login Failed.......")
else:
        data = {}
        data["username"] = input("Username:")
        data['password'] = getpass.getpass()
        rc = r.post("http://wifi.52mianliao.com/", data={
            "action": "login",
            "username": data["username"],
            "password": data["password"]
        }).content.decode()
        p = pq(rc)
        if "登陆用户" in rc:
            # success
            print("Login Success!")
            with open(pass_path, 'w') as fp:
                print("\n".join([i.text for i in p("label")]))
                json.dump(data, fp)
        else:
            print("Login Failed.......")

