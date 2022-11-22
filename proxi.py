import random
from ballyregan import ProxyFetcher
from ballyregan.models import Protocols, Anonymities
import requests

def get_free_proxies():
    fetcher = ProxyFetcher(debug=False)
    # proxiese = fetcher.get_one()
    proxiese = fetcher.get(limit=50,protocols=[Protocols.HTTPS, Protocols.SOCKS5],anonymities=[Anonymities.ELITE])
    return proxiese

def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session, proxy

if __name__=="__main__":
    TimeOut = 5
    Hits = 5000
    print("Getting Proxies....")
    proxiesa=[ip.ip for ip in get_free_proxies()]
    a = input("Type 'Y' to Confirm : ")
    if a in ["Y","y"]:
        print("Starting Hits....")
        for i in range(Hits):
            print(i)
            s,proxy = get_session(proxiesa)
            try:
                req=s.get("https://bits-oasis.org/2022/main/registrations/get_college/", timeout=TimeOut)
                print(req.status_code)
            except Exception as e:
                print(str(e))
                continue
    else:
        print("Aborted.")

