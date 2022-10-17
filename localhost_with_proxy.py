import requests
import random
from bs4 import BeautifulSoup as bs
import time

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"class": "table table-striped table-bordered"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies

def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session, proxy


def get_valid_proxies(proxies):
    NumProxies = 500
    valid_proxies = []
    for i in range(NumProxies):
        s,proxy = get_session(proxies)
        try:
            rr = s.get("http://icanhazip.com", timeout=5)
            if rr.status_code == 200:
                valid_proxies.append(proxy)
        except Exception as e:
            pass
    return list(set(valid_proxies))

if __name__=="__main__":
    TimeOut = 5
    Hits = 5000
    headers = {
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNDYzNiwidXNlcm5hbWUiOiJGcmVzaGVyIiwiZXhwIjoxNjY2NTYyNTQ1LCJlbWFpbCI6ImZyZXNoaWVzQGV4YW1wbGUuY29tIn0.GA0LjNRYLJ_5g2bGwq85LS9f-Oq2GaSU9zWfA9Howhc',
        # 'Cookie': 'csrftoken=kjXAzyvRMMj5fVD0sZBkMKZwBNOQ3KYPvFBtmCIEsgdGzNwzS8T96jR9bO6yyhxO'
    }
    
    print("Getting Proxies....")
    proxies=(get_free_proxies())
    proxies=(get_valid_proxies(proxies))
    print("Validated proxies..")
    time.sleep(15)
    print("Slept 15 secs...")
    a = input("Type 'Y' to Confirm : ")
    if a in ["Y","y"]:
        print("Starting Hits....")
        for i in range(Hits):
            print(i)
            s,proxy = get_session(proxies)
            try:
                req=s.get("https://bitsbosm.org/2022/boco_portal/rounds", timeout=TimeOut, headers=headers)
                print(req.status_code)
            except Exception as e:
                print(str(e))
                continue
    else:
        print("Aborted.")