import requests

def get(g):
    r = requests.get(g)
    s = r.status_code
    t = r.text
    return (s,t)

def post(link,payload):
    r = requests.post(link,payload)
    return (r.text)

def auth(link,payload):
    r = requests.get(link, auth=payload)
    return (r.text)

def put(link,payload):
    r = requests.put(link,payload)
    return (r.text)
