import requests
import threading

Hits = 1
# TimeOut = 3
uRl = "https://bits-oasis.org/2022/main/registrations/events_details/"


def do_it():
    for ind in range(Hits):
        print(ind)
        try:
            req = requests.Session().get(uRl)
            print(req.status_code)
        except Exception as e:
            print(str(e))
            continue


if __name__ == "__main__":
    threads = []
    thth = 1000
    a = input("Type 'Y' to Confirm : ")
    if a in ["Y", "y"]:
        print("Starting Hits....")
        for i in range(thth):
            threads.append(threading.Thread(target=do_it))
        for i in range(thth):
            threads[i].start()
        for i in range(thth):
            threads[i].join()
    else:
        print("Aborted.")
