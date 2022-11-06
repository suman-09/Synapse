import requests

def request(t, url, param, auth, head, json):
    
    if t=="get":
        r = requests.get(url, params=param, auth=auth, headers=head, json=json)
        statcode = r.status_code
        txt = r.text
        hed = r.headers
    if t=="post":
        r = requests.post(url, params=param, auth=auth, headers=head, json=json)
        statcode = r.status_code
        txt = r.text
        hed = r.headers
    if t=="put":
        r = requests.put(url, params=param, auth=auth, headers=head, json=json)
        statcode = r.status_code
        txt = r.text
        hed = r.headers
    if t=="patch":
        r = requests.patch(url, params=param, auth=auth, headers=head, json=json)
        statcode = r.status_code
        txt = r.text
        hed = r.headers
    if t=="delete":
        r = requests.delete(url, params=param, auth=auth, headers=head, json=json)
        statcode = r.status_code
        txt = r.text
        hed = r.headers
    return (statcode, txt, hed)