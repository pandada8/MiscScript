#!/usr/bin/env python3
from sh import ping, osascript, ErrorReturnCode_2, ErrorReturnCode
import time
import tempfile
import os
pingable = True

def say(title, body):
    content = '''display notification "{}" with title "{}"'''.format(body, title)
    fp = tempfile.NamedTemporaryFile("w", delete=False)
    fp.write(content);
    fp.close()
    osascript(fp.name)
    os.unlink(fp.name)
def update_status(status):
    if status != pingable:
        pingable = status
        if status:
            say("ZT 通了", "还不去 Pull 代码")
        else:
            say("ZT 断了", "还不去干活")
    else:
        pass

while True:
    try:
        result = ping("25.25.0.2", _bg=True)
        for i in result:
            if "timeout" in i or "down" in i:
                update_status(False)
            elif "bytes from" in i:
                update_status(True)
    except KeyboardInterrupt:
        raise SystemExit
#from sh import osascript
#a = osascript("-e", r'"display notification "title" with title "name""')
# Why this failed? WTF?
