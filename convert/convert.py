import qrcode
import json
import sys
import os
import base64


def convert(path):
    with open(path) as fp:
        data = json.load(fp)
        s = "{method}:{password}@{server}:{server_port}".format_map(data)
        s = "ss://" + base64.b64encode(s.encode("ASCII")).decode()        
        img = qrcode.QRCode()
        img.add_data(s)
        img.print_ascii(tty=True)

def main():
    if len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
        convert(sys.argv[1])
    else:
        print("Usage:\nconvert.py <config file>")

if __name__ == "__main__":
    main()
