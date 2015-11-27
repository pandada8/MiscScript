from pyquery import PyQuery
import requests
import sys
import os
from urllib.parse import urljoin

def convertLink(origin, base):
    return urljoin(base, origin) if '//' not in origin else origin

def fetchList(link):
    # TODO: make sure the returned content is text/html
    content = requests.get(link)
    if content.status_code == 200:
        pq = PyQuery(content.text)
        a = pq("a")
        hrefs = [convertLink(pq(i).attr("href"), link) for i in a]
        return hrefs
    else:
        return []

def genAria2cList(links):
    return "\n".join(["{}".format(i) for i in links])

def main():
    if len(sys.argv) != 3:
        print("{} <url> <output.list>".format(os.path.split(__file__)[1]))
        raise SystemExit
    link, target = sys.argv[1:]
    files = fetchList(link)
    with open(target, "w") as fp:
        fp.write(genAria2cList(files))

if __name__ == '__main__':
    main()
