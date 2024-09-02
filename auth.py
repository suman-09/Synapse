import requests

class MyAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token


    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer ' + self.token
        return r


if __name__=="__main__":
    
    resp = requests.get('https://httpbin.org/bearer', auth=MyAuth("sometoken"))
