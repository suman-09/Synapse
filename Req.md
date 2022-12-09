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
The flow of the function is as follows:
 1. Setting the variable for taking input from user. Like we make variable url for takin url from the user.
 2. Now setting up the variable for the selected type of request.
     a. Now to get that we define a function got(), where we returned the selected text
     b. And stored the selected test in a variable here in case it is "t"
 3. After that we passed all the necessary inputs to the request function which returns us the Status code, Text and Header response.
 4. we stored all those response in variables here in case statcode for status code, txt is for text and hed for header
 5. Then we just updated the response in the GUI

```
def got():
    selected_dropdown = clicked.get() #to get what the user selected in drop down.
    return(selected_dropdown)

def requested():
    #taking input from user
    url = inputtext.get(1.0, "end-1c") # will be same for param ,auth ,json
    t = got() #the function which stored the selected request type
    statcode, txt, hed = request(t , url, param, auth, head, json)
    response.insert(tk.END , txt) #to update text response in the GUI
    statuscode.config(text = statcode) # to update status code in GUI
```
 - [Requests Documentation](https://pypi.org/project/requests/)
- [beautofulsoup4 Documentation](https://pypi.org/project/beautifulsoup4/)
