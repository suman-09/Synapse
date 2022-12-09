# **PYTHON Setup**
Python is one of the most easy to write and understand programming language. 

The first step to our project is to setup Python in our system, may it be linux, windows or macOS

### **LINUX**
Most linux distros have python preinstalled in them. to find out about the version you have in your system, use the following command in terminal

```
pyhton3 --version
```
if you don't have python preinstalled, you can install it using following command

```
sudo apt-get install python3.6
```
### **WINDOWS**
For windows, all you have to do is download python, and you are good to go and explore this language using any IDLE

Python can be downloaded from the official python website. link below
 __link__: https://www.python.org/downloads/windows/

### **MacOS**
Python can be downloaded for MacOS using the same website.
__link__ : https://www.python.org/downloads/macos/

## **Virtual Environment**

For doing any project, it is always advised to use virtual environment and have all the libraries installed there.
To setup virtual environment, all you have to do in go through the following commands.

### **Linux/Mac setup**

First lets install pip, which will help us in installing other libraries.

```
python3 -m pip install --user --upgrade pip

python3 -m pip --version
```
### Instaling Virtual Environment
Now we will install and start the Virtual Environment for Python. And do to so we need folloing commands

```
python3 -m pip install --user virtualenv
```
### Creating Virtualenv
Once it is installed, its time we create an environment to work in. Use the command below to create a virtualenv
```
python3 -m venv env
```
### Activating a Virtualenv

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

```
source env/bin/activate
```

# **API**
 API is acronym  for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other.

 In this project we are making an application using python that will help in fetching and testing APIs using various libraries of python.
***
 **Approach for building an API Tester**

 This project will enable us to perform the following functions on API:
1. GET
1. POST
1. PUT
1. PATCH
### **GET:**
 A GET request, in simple terms, is a way for you to grab data from a data source with the help of the internet.

### **POST:**

 POST is used to send data to a server to create/update a resource.

### **PUT:**

 PUT is used to send data to a server to create/update a resource.


 The difference between POST and PUT is that PUT requests are idempotent. That is, calling the same PUT request multiple times will always produce the same result. In contrast, calling a POST request repeatedly have side effects of creating the same resource multiple times.
 <!-- ### **AUTH:** 
 Auth is used to add your auth details to the relevant parts of the request when you select or enter them, so you can preview how your data will be sent before you run the request. Your auth data will appear in the relevant parts of the request, for example in the Headers tab. -->
 ### **PATCH:**
 This method is used to update the existing 
 resource  on server and produces new version of existing resource. 
 
 
 The differnce between POST and PATCH is that  POST  updates thhe complete information while PATCH updates some parts of information.   
 ### **DELETE:**
  DELETE request deletes a resource already present in the server. 
***
## In this project we are using mainly the following python libraries:-
 1. REQUESTS
 1. TKINTER
1. TkHTMLView - html page view rendering
1. Tkinter.SimpleDialogue - dialogue box
1. BeautifulSoup from BS4 - html parsing
1. PyWebCopy - response page saving
 ## **REQUESTS**
 ***

One of the main working of this application is to bring data or information from any API and display it to the user. The task of sending HTTP requests using Python is performed using the “Requests” Module. 

 The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

 The first step in using this module is to import it in the python file.

 ### Run the following command to import this library:
```
pip install requests
```
<!-- ### Throughout this project we will be using various functions of **REQUESTS** library for fetching and sending data to server.  -->
### GET:
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
 ```
 Once our HTTP requests are working properly and we are able to fetch data from the API, we need a proper interface to send and receive a request. And for this purpose, we have the Tkinter library in python.
## **TKINTER**
***

 Tkinter is a python library including multiple modules which is used for making GUI for any python application.

### Run the following command to import this library:
```
pip install tkinter
```
Here in this project we are making terminal based GUI.

 Here is the method by  which you can make a frame widget using Tkinter
 
 ```
 root = Tk()
frame = Frame(root)
frame.pack()
frame1 = Frame(root)
frame1.pack( side = BOTTOM )

root.mainloop()
```
Further next here is the way to create a Drop-down menu
```
#Create an instance of tkinter frame
root= Tk()

#Define the size of window or frame
root.geometry("715x250")

#Set the Menu initially
menu= StringVar()
menu.set("Select Any Language")

#Create a dropdown Menu
drop= OptionMenu(root, menu,"C++", "Java","Python","JavaScript","Rust","GoLang")
drop.pack()

root.mainloop()
```
If you want to create a text widget then here is the way
```
root = Tk()
 
# specify size of window.
root.geometry("250x170")
 
# Create text widget and specify size.
T = Text(root, height = 5, width = 52)
```
Tabbed Notebook  widget
```
root = tk.Tk()
root.title("Tab Widget")
title(name)
tabControl = ttk.Notebook(root)
Notebook(master=None, **options)

root.mainloop()
```
Button widget
```
# import everything from tkinter module
from tkinter import *   
 
# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('100x100')
 
# Create a Button
btn = Button(root, text = 'Click me !', bd = '5')
 
# Set the position of button on the top of window.  
btn.pack(side = 'top')   
 
root.mainloop()
```


