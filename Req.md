## **Requested**
 We are going to use the following python libraries to achieve the task
1. Requests
1. beautifulsoup4
## **REQUESTS**
 ***

One of the main working of this application is to bring data or information from any API and display it to the user. The task of sending HTTP requests using Python is performed using the **Requests** Module. 

 The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

 The first step in using this module is to import it in the python file.

 ### Run the following command to import this library:
```
pip install requests
```
***
### **beautifulsoup4**
Beautiful Soup is a library that makes it easy to scrape information from web pages.
We are going to use this libray for parsing HTML.
### Run the following command to import this library:
```
pip install beautifulsoup4
```
***
<!-- ### Throughout this project we will be using various functions of **REQUESTS** library for fetching and sending data to server.  -->
<!-- ### GET:
A simple GET request can be made by REQUESTS library 
```
r = requests.get('url', data={'key': 'value'})
r.status_code
//Displays status code 
r.text
r.json
r.headers
```
here "r" is a Response object,all the information that a user request, will be provided through this object.

### POST:
```
r = requests.post('url', data={'key': 'value'})
```
### PUT:
```
r = requests.put('url', data={'key': 'value'})
```
### PATCH:
```
r = requests.patch(url, params=param, auth=auth, headers=head, json=json)
 ``` -->

## The  ```Requested```   Function
```
import requests
from bs4 import BeautifulSoup as bs

def requested():
    url = "url"
    param = "param"
    auth = "auth"
    head = "head"
    json = "json"
    t = got()
    statcode, txt, hed = request(t , url, param, auth, head, json)
    soup = bs(txt, 'html.parser')
    prettyHTML = soup.prettify()
    lbl1.delete("1.0", "end")
    lbl3.delete("1.0", "end")
    lbl1.insert(tk.END , prettyHTML)
    lbl3.insert(tk.END, hed)
    lbl2.set_html(txt)
    status.config(text = statcode)
    return url
```
 - [Requests Documentation](https://pypi.org/project/requests/)
- [beautofulsoup4 Documentation](https://pypi.org/project/beautifulsoup4/)