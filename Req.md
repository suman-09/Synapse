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

Here the requested function is defined for taking input parameters from user and sending request to server and updating response in GUI.
Inside this function we have defined some variables for taking input like param, auth, head, json ,which are label for parameter input fields.
For various requests like "get", "post" and "patch", we have defined a new variable "t"
After that we have defined a function "got" in which the selected value from drop down will be returned.
As any method is clicked the "got" function is triggered and it commands the variable to save which drop down is selected.
Then all the imput params and selected method is passed in the request funcion.
On the other side request function is returning three new variables "statcode, text, hed" for status code, text and header respectively.
We save those responses in variables and then we configure the output. 

```
def got():
    selected_dropdown = clicked.get()
    return(selected_dropdown)

def requested():
    url = inputtext.get(1.0, "end-1c")
    t = got()
    statcode, txt, hed = request(t , url, param, auth, head, json)
    response.insert(tk.END , txt) #to update text response in the GUI
    statuscode.config(text = statcode) # to update status code in GUI
```
 - [Requests Documentation](https://pypi.org/project/requests/)
- [beautofulsoup4 Documentation](https://pypi.org/project/beautifulsoup4/)
