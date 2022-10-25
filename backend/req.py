import requests

def link(str):
    url = {str}
    print(url)

def get(url):
    r = requests.get(url)
    print(r.status_code)
    print(r.headers)
    
def post(url):
    p = requests.post(url)
    print(p.status_code)            