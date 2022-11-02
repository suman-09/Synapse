import requests

#### request functions

## get Request

# status code of GET request
def scget(url):
    r = requests.get(url)
    s = r.status_code
    return s
# text response of GET request
def txtget(url):
    r = requests.get(url)
    t = r.text
    return t
#  Headers of GET request
def hedget(url):
    r = requests.get(url)
    h = r.headers
    return h

## post request
#status code of POST request
def spost(url,payload):
    r = requests.post(url,  data=payload)
    s = r.status_code
    return s
#text response of POST request
def txtpost(url,payload):
    r = requests.post(url,  data=payload)
    s = r.text
    return s
#  Headers of POST request
def hedget(url,payload):
    r = requests.post(url, data=payload)
    h = r.headers
    return h

## PUT request
#status code of PUT request
def sput(url,payload):
    r = requests.put(url,  data=payload)
    s = r.status_code
    return s
#text response of PUT request
def txtput(url,payload):
    r = requests.put(url,  data=payload)
    s = r.text
    return s   
 
## DELETE request
#status code of DELETE request
def sput(url,payload):
    r = requests.delete(url,  data=payload)
    s = r.status_code
    return s
#text response of DELETE request
def txtput(url,payload):
    r = requests.delete(url,  data=payload)
    s = r.text
    return s    
          
# def get(g):
#     r = requests.get(g)
#     s = r.status_code
#     t = r.json()
#     return (s,t)

# def post(link,payload):
#     r = requests.post(link,payload)
#     return (r.text)

# def auth(link,payload):
#     r = requests.get(link, auth=payload)
#     return (r.text)

# def put(link,payload):
#     r = requests.put(link,payload)
#     return (r.text)
