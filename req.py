import requests

def get(str):
    r = requests.get(str)
    s = r.status_code
    t = r.text
    return (s,t)
