import requests
import json
from auth import MyAuth

def headerfxn(head):
    
    # converting the header from string type to dictionary type
    header = json.loads(head)
    return header

def request(t, url, param, auth_token, head, json):
    
    # checking if header has any argument or not
    while len(head)>1 :
        jsheader = headerfxn(head)
        break
    else :
        jsheader = head  
      
    if t=="get": 
        r = requests.get(url, params=param, auth=MyAuth(auth_token), headers=jsheader, json=json)
        statcode = r.status_code
        txt = r.text
        hed = r.headers
    if t=="post":
        r = requests.post(url, params=param, auth=MyAuth(auth_token), headers=jsheader, json=json)
        statcode = r.status_code
        txt = r.text
        hed = r.headers
    if t=="put":
        r = requests.put(url, params=param,auth=MyAuth(auth_token), headers=jsheader, json=json)
        statcode = r.status_code
        txt = r.text
        hed = r.headers
    if t=="patch":
        r = requests.patch(url, params=param,auth=MyAuth(auth_token), headers=jsheader, json=json)
        statcode = r.status_code
        txt = r.text
        hed = r.headers
    if t=="delete":
        r = requests.delete(url, params=param,auth=MyAuth(auth_token), headers=jsheader, json=json)
        statcode = r.status_code
        txt = r.text
        hed = r.headers
    return (statcode, txt, hed)